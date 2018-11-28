#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

int solve(string str, int K){
  int ret = 0;
  rep(i,str.length()-K+1){
    if(str[i] == '-'){
      ret++;
      rep(j,K){
        if(str[i+j]=='+') str[i+j] = '-';
        else str[i+j] = '+';
      }
    }
  }
  rep(i,str.length()){
    if(str[i] == '-') return -1;
  }
  return ret;
}

int main(){
  int T;
  cin >> T;
  rep(t,T){
    string str;
    int K;
    cin >> str >> K;

    int ret = solve(str, K);
    
    if(ret < 0){
      cout << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
    }else{
      cout << "Case #" << t+1 << ": " << ret << endl;
    }
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
