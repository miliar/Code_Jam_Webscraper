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

int t = 1, tt;
ll k, c, s, tam, pos;

int main()
{
	scanf("%d", &tt);
	while(tt--)
	{
		printf("Case #%d:", t++);
		scanf("%lld %lld %lld", &k, &c, &s);
		pos = 0;
		tam = 1;
		for(int i = 0; i < c-1; ++i)
			tam *= k;
		for(int i = 1; i <= k; ++i)
		{
			printf(" %lld", i+pos);
			pos += tam-1;
		}
		printf("\n");
	}

	return 0;
}