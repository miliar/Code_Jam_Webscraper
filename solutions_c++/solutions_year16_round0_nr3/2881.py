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


int f(ll x)
{
	for(int i = 2; i <= sqrt(x)+1 && i < x; ++i)
		if(x%i == 0) return i;
	return -1;
}

vi aux;
vector<vi> v;

bool t(int x)
{
	aux.clear();
	aux.pb(x);
	for(ll base = 2; base <= 10; ++base)
	{
		ll y = 0, b = 1, xx = x;
		while(xx > 0)
		{
			y += (xx&1)*b;
			b *= base;
			xx >>= 1;
		}
		xx = f(y);
		if(xx == -1) return false;
		else aux.pb(xx);
	}
	return true;
}

int main()
{
	printf("Case #1:\n");
	int rest = 50;
	for(int i = (1<<15)+1; i < (1<<16) && rest; i += 2)
	{
		if(t(i))
		{
			v.pb(aux);
			rest--;
		}
	}
	for(int i = 0; i < 50; ++i)
	{
		int x = v[i][0];
		for(int j = 15; j >= 0; --j)
			printf("%d", (x&(1<<j))>0);
		for(int j = 1; j < v[i].size(); ++j)
			printf(" %d", v[i][j]);
		printf("\n");
	}

	return 0;
}