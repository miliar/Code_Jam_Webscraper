#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MXN=10004;

int n;
int h[MXN];

int solve()
{
  int ans = 0;
  int l =0, r= n-1;
  while (l < r) {
    int minp = l;
    int minv = h[l];
    for (int j=l; j<=r; j++) {
      if (h[j] < minv) {
        minv = h[j];
        minp = j;
      }
    }
      if (minp-l < r-minp) {
        ans += minp-l;
        for (int i=minp; i>l; i--) {
          h[i] = h[i-1];
        }
        l++;
      } else {
        ans += r-minp;
        for(int i=minp; i<r; i++) {
          h[i] = h[i+1];
        }
        r--;
      }
  }
  return ans;
}

int main()
{
  int t;
  cin >> t;
  for (int i=1; i<=t; i++) {
    cin >> n ;
    for (int j=0; j<n; j++)cin >> h[j];
    cout << "Case #" << i << ": " << solve() << "\n";
  }
  return 0;
}
