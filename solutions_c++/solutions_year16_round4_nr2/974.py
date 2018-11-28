#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
typedef pair<int,int> ii;

#define fi first
#define se second
#define pb push_back
#define mp make_pair

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;

ld prob[201];

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("B-small-attempt0 (2).in", "r", stdin);
	freopen("GCJ20162B.out", "w", stdout);
	int t; cin >> t;
	int T = 0;
	while(t--)
	{
		T++;
		int n, k;
		cin >> n >> k;
		for(int i = 0; i < n; i++)
		{
			cin >> prob[i];
		}
		int s = (1 << k) - 1;
		ld res = 0;
		while (!(s & (1<<n)))
		{
			// do stuff with s
			ld ans = ld(0);
			vi vec;
			
			for(int i = 0; i < n; i++)
			{
				if(s & (1<<i)) vec.pb(i);
			}
			int ss = (1 << (k/2)) - 1;
			while (!(ss & (1<<(k))))
			{
				// do stuff with s
				ld tmp = ld(1);
				for(int j = 0; j < k; j++)
				{
					if(ss & (1<<j))
					{
						tmp *= prob[vec[j]];
					}
					else
					{
						tmp *= (ld(1) - prob[vec[j]]);
					}
				}
				ans += tmp;
				int loo = ss & ~(ss - 1);       // lowest one bit
				int lzz = (ss + loo) & ~ss;      // lowest zero bit above lo
				ss |= lzz;                     // add lz to the set
				ss &= ~(lzz - 1);              // reset bits below lz
				ss |= (lzz / loo / 2) - 1;      // put back right number of bits at end
			}
			res = max(ans, res);
			int lo = s & ~(s - 1);       // lowest one bit
			int lz = (s + lo) & ~s;      // lowest zero bit above lo
			s |= lz;                     // add lz to the set
			s &= ~(lz - 1);              // reset bits below lz
			s |= (lz / lo / 2) - 1;      // put back right number of bits at end
		}
		cout << "Case #" << T << ": ";
		cout << fixed << setprecision(10) << res;
		cout << '\n';
	}
	return 0;
}
