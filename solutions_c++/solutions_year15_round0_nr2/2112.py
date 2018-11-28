#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <bitset>
#include <utility>
#include <iomanip>
#include <set>
#include <fstream>
#include <numeric>
#include <stdexcept>
#include <cassert>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 2000000000
#define PI acos(-1.0)
#define EPS 1e-8
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))

using namespace std;

int n;
int arr[1005];

int main()
{
  ios_base::sync_with_stdio(0);
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    cin >> n;
    for(int i=0;i<n;i++)
      cin >> arr[i];
    int L = 0, R = 1005;
    while(R > L)
    {
      int mid = L + (R - L) / 2;
      bool test = false;
      for(int i=1;i<=mid && !test;i++)
      {
        int cnt = 0;
        for(int j=0;j<n;j++)
          cnt+=(arr[j] + i - 1) / i - 1;
        if(cnt + i <= mid) test = true;
      }
      if(test) R = mid;
      else L = mid + 1;
    }
    cout << "Case #" << tt++ << ": " << L << "\n";
  }
  return 0;
}
