#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <iostream>
#include <vector>
#include <climits>
#include <complex>
#include <sstream>
#include <utility>
#include <valarray>
#include <string>
#include <queue>
#include <iterator>
#include <cstring>

#define rep(i, a, n) for (i = a; i < n; i++)
#define repd(i, n, a) for(i = n; i > a; i--)


#define MOD 1000000007
typedef long long int LL;
using namespace std;
vector <LL> a;
LL n;

int main()
{
	ios::sync_with_stdio(false);
	freopen("/home/spharish/input.txt", "r", stdin);
	freopen("2.out", "w", stdout);
	int tc;
	LL ans;
	
	cin >> tc;
	for (LL k = 0; k < tc; ++k)
	{
		
		cin >> n;
		a.clear();
		for (LL j = 0; j < n; ++j)
		{
			LL tmp;
			cin >> tmp;
			a.push_back(tmp);
		}
		sort(a.begin(),a.end());
		reverse(a.begin(),a.end());
		LL ans = INT_MAX;
		for (LL i = 1; i <= 1000; ++i)
		{
			LL ct = 0;
			for (LL j = 0; j < n; ++j)
			{
				if (a[j] > i and (a[j] - i) % i == 0) {
					ct += (a[j] - i) / i;
				}
				else if (a[j] > i) {
					ct += (a[j] - i) / i + 1;
				}
			}
			ans = min(ans, i+ct);
		}
		cout << "Case #" << k+1 << ": " << ans << endl;
	}
	return 0;
}