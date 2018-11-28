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

int tt, t = 1;
char s[111];
int n;
int pd[111][111][2][2][2];

int f(int i, int j, int x, int l, int fim)
{
	if(i > j) return 0;
	int &p = pd[i][j][x][l][fim];
	if(p == inf)
	{
		if(!l)
			p = min(p, 1+f(i, j, x^1, 1, fim));
		
		if(!x)
		{
			if(s[j]^fim^x)
				p = min(p, f(i, j-1, x, 0, fim));
			else
				p = min(p, 1+f(i, j-1, x, 0, fim^1));
		}
		else
		{
			if(s[i]^fim^x)
				p = min(p, f(i+1, j, x, 0, fim));
			else
				p = min(p, 1+f(i+1, j, x, 0, fim^1));
		}		
	}
	return p;
}

int main()
{
	scanf("%d", &tt);
	while(tt--)
	{
		scanf("%s", s);
		n = strlen(s);
		for(int i = 0; i < n; ++i)
			s[i] = (s[i] == '+');
		memset(pd, inf, sizeof pd);
		printf("Case #%d: %d\n", t++, f(0, n-1, 0, 0, 0));
	}

	return 0;
}