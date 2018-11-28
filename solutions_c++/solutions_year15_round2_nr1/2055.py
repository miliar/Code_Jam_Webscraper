#include <sstream>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
int tbl[10000001];
queue<int> q;
int rev(int x){
  stringstream a,b;
  a << x;
  string s;
  a >> s;
  reverse(s.begin(),s.end());
  b << s;
  int ret; b >> ret;
  return ret;
}

int solve(int n){
  if(tbl[n]) return tbl[n];
  if(!tbl[1]){
    q.push(1);
    tbl[1]=1;
  }
  while(!q.empty()){
    int x = q.front();q.pop();
    if(x>=10000000) continue;
    int nxt1 = x+1;
    int nxt2 = rev(x);
    if(!tbl[nxt1]){
      q.push(nxt1);
      tbl[nxt1]=tbl[x]+1;
    }
    if(!tbl[nxt2]){
      q.push(nxt2);
      tbl[nxt2]=tbl[x]+1;
    }
  }
  return tbl[n];
}
int main(){
  int T; cin>>T;
  for(int i=2;i<=1000000;++i) if(!tbl[i]) tbl[i]=solve(i);
  for(int t=1;t<=T;++t){
    int n;
    cin >> n;
    cout << "Case #"<<t<<": " << solve(n) << endl;
  }
  return 0;
}
