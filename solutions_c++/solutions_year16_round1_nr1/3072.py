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

int t, tt, n;
char s[1010];
char ans[1010];

struct no
{
	char c;
	int pos;
	no() {}
	no(char c, int pos): c(c), pos(pos) {}
	bool operator < (no a) const
	{
		if(c != a.c) return c > a.c;
		return pos > a.pos;
	}
} v[1010];
int main()
{
	scanf("%d", &tt);
	t = 1;
	while(tt--)
	{
		scanf("%s", s);
		n = strlen(s);

		for(int i = 0; i < n; ++i)
			v[i] = no(s[i], i);
		sort(v, v+n);
		int a = 0, b = n-1, last = n-1;
		for(int i = 0; i < n; ++i)
		{
			if(v[i].pos > last) continue;
			while(last > v[i].pos) ans[b--] = s[last--];
			ans[a++] = v[i].c;
			last--;
		}

		ans[n] = 0;
		printf("Case #%d: %s\n", t++, ans);
	}

	return 0;
}