/*
ID: jeffrey31
LANG: C++
TASK: B
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;

const int N  = 1010;
int t;
int n, a[N], f[N];

int main() {
  freopen("B.in","r",stdin);
  freopen("B.out","w", stdout);
  cin >> t;
  for(int i = 1; i <= t; i++) {
    int ans = 100000000;
    printf("Case #%d: ", i);
    cin >> n;
    memset(a, 0, sizeof(a));
    memset(f, 0, sizeof(f));
    for(int j = 0; j < n; j++) {
      cin >> a[j];
    }
    for(int j = 1; j <= 1000; j++) {
      for(int k = 0; k < n; k++) {
        f[j] += (a[k] - 1) / j;
      }
      ans = min(ans, j + f[j]);
    }
    cout << ans << endl;
  }
  
  return 0;
}