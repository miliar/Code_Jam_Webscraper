#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>

using namespace std;

int r, p, s, n;

int nCk(int n, int k){
  if(k == 0)return 1;
  return nCk(n, k-1) * (n - k + 1) / k;
}

int ans[1 << 12];

string output(char x, int n){
  string res = "";
  res += x;
  if(n == 0)return res;
  char lose;
  string tmp1 = output(x, n-1);
  if(x == 'R')lose = 'S';
  if(x == 'S')lose = 'P';
  if(x == 'P')lose = 'R';
  string tmp2 = output(lose, n-1);
  if(tmp1 > tmp2)return tmp2 + tmp1;
  else return tmp1 + tmp2;
}

void solve(){
  cin >> n >> r >> p >> s;
  int cnt[] = {0, 0, 0};
  for(int i = 0;i <= n;i++){
    cnt[i % 3] += nCk(n, i);
  }
  if(cnt[0] == r && cnt[1] == s && cnt[2] == p){
    cout << output('R', n) << endl; 
    return;
  }

  if(cnt[0] == s && cnt[1] == p && cnt[2] == r){
    cout << output('S', n) << endl;
    return;
  }

  if(cnt[0] == p && cnt[1] == r && cnt[2] == s){
    cout << output('P', n) << endl;
    return;
  }
  cout << "IMPOSSIBLE" << endl;
  return;
}

void init(){
  ans[0] = 0;
  for(int i = 0;i < 12;i++){
    for(int j = 1 << i; j < (1 << (i+1)); j++){
      ans[j] = (ans[j - (1 << i)] + 1) % 3;
    }
  }
}

int main(){
  init();
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
