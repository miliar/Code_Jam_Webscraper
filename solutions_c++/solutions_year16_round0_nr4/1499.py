#include<bits/stdc++.h>
using namespace std;

void solve(int k,int c,int s){
  for(int i = 1;i <= k;++i){
    cout << " " << i;
  }
  cout << endl;
}

int main(void){
  int t;
  cin >> t;
  for(int i = 1;i <= t;++i){
    cout << "Case #" << i << ":";
    int k,c,s;
    cin >> k >> c >> s;
    solve(k,c,s);
  }
  return 0;
}
