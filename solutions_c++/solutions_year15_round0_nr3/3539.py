#include <bits/stdc++.h>
using namespace std;

int l,x;
vector<int> v;
map<char,int> mp;


void make(){
  mp.clear();
  mp['1'] = 1;
  mp['i'] = 2;
  mp['j'] = 3;
  mp['k'] = 4;
}

bool solve(){
  vector<int> v1,v2;
  int op[5][5] = {{0, 0, 0, 0, 0},
                  {0, mp['1'], mp['i'], mp['j'], mp['k']},
                  {0, mp['i'], -mp['1'], mp['k'], -mp['j']},
                  {0, mp['j'], -mp['k'], -mp['1'], mp['i']},
                  {0, mp['k'], mp['j'], -mp['i'], -mp['1']}};
  int now = v[0];

  if(v.size() <= 2) return false;
  
  if(now == mp['i']) v1.push_back(0);
  for(int i=1;i<v.size();i++){
    int a = now, b = v[i];    
    if(a > 0 && b < 0 || a < 0 && b > 0){
      a = abs(a);
      b = abs(b);
      now = -op[a][b];
    } else {
      a = abs(a);
      b = abs(b);
      now = op[a][b];
    }
    if(now == mp['i']) v1.push_back(i);
  }

  now = v[v.size()-1];
  if(now == mp['k']) v2.push_back(v.size()-1);
  for(int i=v.size()-2;i>=0;i--){
    int a = v[i], b = now;
    if(a > 0 && b < 0 || a < 0 && b > 0){
      a = abs(a);
      b = abs(b);
      now = -op[a][b];
    } else {
      a = abs(a);
      b = abs(b);
      now = op[a][b];
    }
    if(now == mp['k']) v2.push_back(i);
  }
  reverse(v2.begin(), v2.end());

  for(int i=0;i<v1.size();i++){
    int st = v1[i] + 1;
    now = -100;
    for(int j=0;j<v2.size();j++){
      int go = v2[j] - 1;
      if(st > go) continue;
      if(now == -100) now = v[st];
      for(int k=st;k<go;k++){
        int a = now, b = v[k+1];
        if(a > 0 && b < 0 || a < 0 && b > 0){
          a = abs(a);
          b = abs(b);
          now = -op[a][b];
        } else {
          a = abs(a);
          b = abs(b);
          now = op[a][b];
        }
      }
      if(now == mp['j']) return true;
      st = go;
    }
  }
  return false;
}

int main(){
  int T;
  cin >> T;
  make();
  for(int t=1;t<=T;t++){
    string s;
    v.clear();
    cin >> x >> l;
    cin >> s;
    for(int i=0;i<l;i++) {
      for(int j=0;j<x;j++){
        v.push_back(mp[s[j]]);
      }
    }
    cout << "Case #" << t << ": " << (solve() ? "YES" : "NO") << endl;
  }
}
