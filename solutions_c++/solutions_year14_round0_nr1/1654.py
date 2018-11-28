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

int T, row, val;

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
    	int mask = (1<<16) - 1;
    	for (int i = 0; i < 2; ++i)
    	{
    		cin >> row, --row;
    		int m = 0;
			for (int j = 0; j < 4; ++j)
			for (int k = 0; k < 4; ++k)
			{
				cin >> val, --val;
				if (j == row)
					m |= 1<<val;
			}
			mask &= m;
    	}    	
    	cout << "Case #" << z << ": ";
    	if (mask == 0)
    		cout << "Volunteer cheated!" << endl;
    	else if (mask != (mask & -mask))
    		cout << "Bad magician!" << endl;
    	else
    	{
    		int ans = 0;
    		while (mask)
    			mask /= 2, ++ans;
    		cout << ans << endl;
    	}
    }
}
