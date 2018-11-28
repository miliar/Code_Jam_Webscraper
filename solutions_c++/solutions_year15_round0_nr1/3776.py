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
char a[1004];
int main()
{
	//freopen("1.in", "r", stdin);
			//freopen("/home/spharish/input.txt", "r", stdin);
	//freopen("1_ans_large.out", "w", stdout);
	int tc;
	cin >> tc;
	for (LL i = 0; i < tc; ++i)
	{
		LL n;
		LL ans = 0;
		LL cur = 0;
		cin >> n;
		
		scanf("%s", a);
		cur = a[0] - '0';
		for (LL j = 1; j <= n; ++j)
		{
			if (a[j] - '0' != 0) {
				if (cur < j) {
					ans += j - cur;
					cur += (j - cur) + (a[j] - '0');
				}
				else {
					cur += (a[j] - '0');
				}
			}


		}

		cout << "Case #" << i+1 << ": " << ans << endl;

		
	}
	return 0;
}