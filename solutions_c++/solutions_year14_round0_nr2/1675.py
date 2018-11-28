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

ld T, C, F, X;

int main()
{
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(9);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
    	cin >> C >> F >> X;
    	ld ans = 0, rate = 2;
    	while (X*F > C*(rate+F))
    	{
    		ans += C / rate;
    		rate += F;
    	}
    	ans += X / rate;
    	cout << "Case #" << z << ": ";
    	cout << ans << endl;
    }
}
