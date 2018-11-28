#include <bits/stdc++.h>

#define maxn 200100
#define logn 23
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define mod 1000000007LL

using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

int t;
ll n;
int v[10];

int main()
{
	scanf("%d", &t);
	for(int tt = 1; tt <= t; ++tt)
	{
		printf("Case #%d: ", tt);
		scanf("%lld", &n);
		memset(v, 0, sizeof v);
		ll ans = -1;
		for(int i = 1; i <= 100000 && ans == -1; ++i)
		{
			int x = i*n;
			do
			{
				v[x%10]++;
				x /= 10;
			} while(x > 0);
			int ok = 0;
			for(int j = 0; j < 10; ++j)
			{
				ok += v[j]>0;
			}
			if(ok==10) ans = i;
		}
		if(ans == -1) printf("INSOMNIA\n");
		else printf("%lld\n", ans*n);
	}

	return 0;
}