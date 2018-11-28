#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int T, D, P[1000];

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
    	cin >> D;
    	for (int i = 0; i < D; ++i)
    	    cin >> P[i];
    	sort(P, P+D);
    	int ans = P[D-1];
    	for (int rem = 1; rem < ans; ++rem)
    	{
    	    int t = rem;
    	    for (int i = 0; i < D; ++i)
    	        t += (P[i]-1)/rem;
    	    ans = min(ans, t);
    	}
    	cout << "Case #" << z << ": " << ans << endl;
    }
}
