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

int main()
{
  ios_base::sync_with_stdio(0);
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int x, n, m;
    cin >> x >> n >> m;
    bool test = false;
    if(n < m) swap(n, m);
    if((n * m) % x != 0 || (x >= 7))
      test = true;
    else if(n == 4 && m <= 2 && x == 4)
      test = true;
    else if(n == 3 && m == 1 && x == 3)
      test = true;
    else if(n == 2 && m == 2 && x == 4)
      test = true;
    cout << "Case #" << tt++ << ": " ;
    if(test) cout << "RICHARD\n";
    else cout << "GABRIEL\n";
  }
  return 0;
}
