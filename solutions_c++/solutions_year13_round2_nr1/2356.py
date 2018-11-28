//Seikang

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <stdlib.h>
#include <assert.h>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>

#include <cmath>
#include <complex>
#include <algorithm>

#include <ctime>
#define gtime clock()

using namespace std;

#define SZ(cont) (int)(cont.size())
#define ALL(cont) (cont).begin(), (cont).end()
#define DEBUG(x) cerr << ">" << #x << ":" << x << endl

typedef long long int64;
typedef pair<int64, int64> ii;
typedef vector<int64> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo32 = 1ll << 30, oo64 = 1ll << 60;
const double pi = acos(-1.0), eps = 1e-9;
inline bool equal(const double &a, const double &b){return abs(a - b) < eps;}

int calc(int64 sum, int64 target)
{
	if(sum == 1)
		return oo32;
	int ans = 0;
	while(sum <= target)
	{
		sum += sum - 1;
		assert(sum >= 0);
		ans++;
	}
	return ans;
}
int main()
{
	//freopen ("in.txt", "rt", stdin);
	//freopen ("A.out", "wt", stdout);

	int T; cin >> T;
	for(int t = 0; t < T; t++)
	{
		int64 m, n;
		cin >> m >> n;
		vi num(n);
		for(int i = 0; i < n; i++)
		{
			cin >> num[i];
		}
		sort(ALL(num));
		int ans = 0;
		for(int i = 0; i < n; i++)
		{
			int c = calc(m, num[i]);
			if(c >= n - i)
			{
				ans += n - i;
				break;
			}
			ans += c;
			for(int j = 0; j < c; j++)
			{
				m += m - 1;
			}
			m += num[i];
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
