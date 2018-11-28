/*************************************************************************
  > File Name: b.cpp
  > Author: implus
  > Mail: 674592809@qq.com
  > Created Time: 日  5/11 17:54:33 2014
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define ls (rt<<1)
#define rs (rt<<1|1)
#define lson l,m,ls
#define rson m+1,r,rs


const ll MOD = 1e9 + 7;

int T, n;
struct node{
  string s; ll v;
  node(){} node(string s, ll v):s(s), v(v){}
  void one(){
    int i = 0, j = 0;
    string ns;
    for(; i < s.size(); i = j){
      j = i;
      while(j < s.size() && s[j] == s[i]) j++;
      ns += s[i];
    }
    s = ns;
  }
};
char ch[11111];

bool check(string s){
  vector<int> cnt(33, 0);
  for(int i = 0; i < s.size(); i++){
    cnt[s[i] - 'a']++;
    if(cnt[s[i] - 'a'] >= 2) return 0;
  }
  return 1;
}

bool isAll(string s, char c){
  for(int i =0; i < s.size(); i++){
    if(c != s[i]) return 0;
  }
  return 1;
}

bool isBegin(string s, char c){
  return s[s.size() - 1] == c;
}
bool isEnd(string s, char c){
  return s[0] == c;
}


bool has(string s, char c){
  for(int i = 0; i < s.size(); i++) if(s[i] == c) return 1;
  return 0;
}
bool gao(vector<node> vn){
  for(int i = 0; i < vn.size(); i++){
    if(check(vn[i].s) == 0) return 1;
  }
  for(char c = 'a'; c <= 'z'; c++){
    int cnt = 0;
    for(int i = 0; i < vn.size(); i++){
      if(has(vn[i].s, c)) cnt++;
    }
    if(cnt >= 2) return 1;
  }
  return 0;
}

ll A[111];
int main(){
  scanf("%d", &T);
  int icase = 1;
  A[0] = 1;
  for(int i = 1; i < 111; i++){
    A[i] = A[i - 1] * i;
    A[i] %= MOD;
  }

  while(T--){
    scanf("%d", &n);
    vector<node> lx(n);
    for(int i = 0; i < n; i++){
      scanf("%s", ch);
      lx[i] = node(ch, 1);
      lx[i].one();
    }
    bool ok = 1;
    for(int i = 0; i < n; i++){
      if(check(lx[i].s) == 0) {
        ok = 0; break;
      }
    }
    for(int i = 0; i < 26; i++)if(ok){// gao char
      vector<node> end;
      vector<node> begin;
      vector<node> all;
      vector<node> other;
      for(int j = 0; j < lx.size(); j++){
        if(isAll(lx[j].s, 'a' + i)){
          all.push_back(lx[j]);
        }else if(isBegin(lx[j].s, 'a' + i)){
          begin.push_back(lx[j]);
        }else if(isEnd(lx[j].s, 'a' + i)){
          end.push_back(lx[j]);
        }else other.push_back(lx[j]);
      }

      if(begin.size() >= 2 || end.size() >= 2){
        ok = 0; break;
      }
      string s = ""; ll v = 1;
      if(begin.size() == 1){
        s += begin[0].s;
        v *= begin[0].v;
        v %= MOD;
      }

      for(int j = 0; j < all.size(); j++){
        s += all[j].s;
        v *= all[j].v; v %= MOD;
      }
      v *= A[all.size()], v %= MOD;

      if(end.size() == 1){
        s += end[0].s;
        v *= end[0].v;
        v %= MOD;
      }
      
      lx = other;
      if(s != "") {
        node nn = node(s, v); nn.one();
        lx.push_back(nn);
        //cerr<<"new node = "<<s<<" v = "<<v<<endl;
      }
      
    }

    if(ok==0 || gao(lx)){
      printf("Case #%d: 0\n", icase++);
      continue;
    }

    ll ans = 1;
    for(int i = 0; i < lx.size(); i++){
      ans *= lx[i].v, ans %= MOD;
      //cerr<<"lx[i].v = "<<lx[i].v<< " s= "<<lx[i].s<<endl;
    }
    ans *= A[lx.size()], ans %= MOD;
    printf("Case #%d: %lld\n", icase++, ans);

  }
  return 0;
}
