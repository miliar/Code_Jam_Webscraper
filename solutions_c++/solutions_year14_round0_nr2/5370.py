#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <assert.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);


void solve(int test)
{
   ld c, f, x;
   cin >> c >> f >> x;
   ld ct = 0., cs = 2., cc = 0.;
   ld ans = x/cs;
   for (int i = 0; i < 3000000; i++)
   {
      ans = min(ans, ct + (x-cc)/cs);
    //  assert(cc < 1e-9);
      ct += (c-cc)/cs;
      cs += f;
      cc = 0.;
   }
   cout.precision(15);
   cout << "Case #" << test << ": " << ans << endl;
}

int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++) solve(i);
}