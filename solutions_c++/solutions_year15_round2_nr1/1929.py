#include<iostream>
#include<algorithm>

using namespace std;

bool done[1000001];
long long dp[1000001];

long long rev(long long n) {
  long long ans = 0;
  while (n>0) {
    long long d = n%10;
    ans = ans*10 + d;
    n/=10;
  }
  return ans;
}

long long solve(long long n, long long cur) {
  dp[1]=1;
  done[1] = true;
  for (long long i=2; i<=n; i++) {
        done[i] = true;
    long long a1 = i-1;
    long long a2 = rev(i);
    if (a2<i && rev(a2)==i) {
      dp[i] = 1+min(dp[a1],dp[a2]);
    }
    else {
      dp[i] = 1+dp[a1];
    }
  }
  return dp[n];
}

int main() {
  int t; cin >> t;
  for (int i=0; i<t; i++) {
    for (int j=0; j<1000000; j++) {
      done[j]=false;
      dp[j]=10000000;
    }
    long long n; cin >> n;
    long long ans = 1;
    long long cur = 1;
    ans  = solve(n,cur);
    cout << "Case #" << i+1 << ": " << ans << endl;
  }

  return 0;
}
