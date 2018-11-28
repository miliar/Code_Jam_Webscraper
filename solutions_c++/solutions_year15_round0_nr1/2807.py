#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;


int solve() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  int maxim = 0;
  int sum = 0;
  for(int i=0; i<n+1; i++) {
    maxim = max(maxim, i - sum); 
    sum = sum + s[i] - '0';
  }
  return maxim;
}

int main() {
  int n;
  cin >> n;
  for(int i=0; i<n; i++) {
    int ans = solve();
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  
  return 0;
}
