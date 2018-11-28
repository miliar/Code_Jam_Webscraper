// created by: Prashant Kumar Singh :)
#include<iostream>
#include<algorithm>
#include<utility>
#include<cstring>
#include<string.h>
#include<set>
#include<map>
#include<math.h>
#include<stdio.h>
#include<vector>
#include<functional>
#include<bitset>
#include<iomanip>
#define ll long long
#define gr greater<ll>()
#define pi acos(-1.0)
#define pb push_back
#define MS0(ar) memset(ar,0,sizeof ar)
#define f first
#define s second
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ind(a) scanf("%d",&a)
#define inf(a) scanf("%lf",&a)
#define inl(a) scanf("%lld",&a)
#define ins(a) scanf("%s",a)
#define pd(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a);
#define bitcnt(x) __builtin_popcountll(x)
using namespace std;
int vis[10];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
/*#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
#endif
	freopen("output.txt", "w", stdout);
*/	ll t, k = 0, n;
	cin >> t;
	while (t--)
	{
		cin >> n;
		ll i = 1, flag = 0;
		k++;
		if (n == 0)
		{
			cout << "Case #" << k << ": " << "INSOMNIA" << endl;
			continue;
		}
		MS0(vis);
		while (!flag)
		{
			ll x = n * i;
			//cout << x << endl;
			while (x > 0)
			{
				vis[x % 10] = 1;
				x /= 10;
			}
			int ntr = 0;
			for (int y = 0; y <= 9; y++)
			{
				if (!vis[y])
					ntr = 1;
			}
			if (ntr)
				flag = 0;
			else
				flag = 1;
			if (flag)
				break;
			i++;
		}
		cout << "Case #" << k << ": " << i*n << endl;
	}
	return 0;
}