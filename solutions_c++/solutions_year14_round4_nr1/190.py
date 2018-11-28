#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MXN=10004;

int n;
int h[MXN];
int x;
int solve()
{
  sort(h, h+n);
  int l =0;
  int r = n-1;
  int ans = 0;
  while (l <r) {
    while (l <r && h[l]+h[r] > x) {
      ans++;
      r--;
    }
    l++;
    r--;
    ans++;
  }
  if (l == r)ans++;
  return ans;
}

int main()
{
  int t;
  cin >> t;
  for (int i=1; i<=t; i++) {
    cin >> n >> x;
    for (int j=0; j<n; j++)cin >> h[j];
    cout << "Case #" << i << ": " << solve() << "\n";
  }
  return 0;
}
