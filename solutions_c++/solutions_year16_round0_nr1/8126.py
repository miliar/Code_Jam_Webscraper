#include <bits/stdc++.h>
using namespace std;
long long solve(long long);
long long dp[1000006];
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    /*
    for (long long i=1; i<=1000000; i++) {
      dp[i] = solve(i);
    }*/
    long long t;
    cin>>t;
    for (long long i=0; i<t; i++) {
      long long n;
      cin>>n;
      long long ans = solve(n);
      cout<<"Case #"<<i+1<<": ";
      ans ? cout<<ans<<endl : cout<<"INSOMNIA"<<endl;
    }
    return 0;
}

set<long long> ss;
void processDigits(long long temp) {
    while (temp) {
      ss.insert(temp%10);
      temp /= 10;
    }
}
long long solve(long long n) {
  ss.clear();
  long long temp;
  if (n==0) {
    return 0;
  }
  for (long long i=1; i<=100; i++) {
    temp = i*n;
    processDigits(temp);
    if (ss.size() == 10)
      break;
  }
  assert(ss.size() == 10);
  return temp;
}
