#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <memory.h>
#include <sstream> 
#include <string>
#include <set>
#include <queue>
#include <map>
#include <vector>
#include <ctime>
#include <bitset>
#include <cassert>
#include <iomanip>
using namespace std;

#define forn(i,n)  for(int i = 0; i < (n); ++i) 
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define fskfs x
#define sfdjh y
#define pii pair<int, int> 
#define mod 1000000007
#define inf 2000000000
#define eps 1e-8
#define sq(x) ((x) * (x))
typedef long long ll; 

vector<int>a;
string s;
int n;
void init ()
{
    cin >> n >> s;
    ++n;
    a.resize(n);
    for (int i = 0; i < n; ++i)
        a[i] = s[i] - '0';
}

void solve ()
{
    int ans = 0, sum = a[0];
    for (int i = 1; i < n; ++i)
    {
        if (i > sum)
        {
            ans += i - sum;
            sum += i - sum;
        }
        sum += a[i];
    }
    cout << ans << '\n';
}
int main()
{
   //freopen("A-large.in", "rt", stdin); freopen("output.txt", "wt", stdout);
   ios_base::sync_with_stdio(false); cin.tie(0);
   int T;
   cin >> T;
   for (int i = 1; i <= T; ++i)
   {
       cout << "Case #" << i << ": ";
       init();
       solve();
   }
 return 0;

}