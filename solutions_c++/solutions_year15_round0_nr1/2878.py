#include <bits/stdc++.h>

#define maxn 1010
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

int n;
int teste = 1;
int t;
int ans, x;
char s[maxn];

int main()
{
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d %s", &n, s);
		ans = 0;
		x = 0;
		for(int i = 0; i <= n; ++i)
		{
			s[i] -= '0';
			if(x >= i)
			{
				x += s[i];
			}
			else
			{
				ans += i-x;
				x += i-x + s[i];
			}
		}
		printf("Case #%d: %d\n", teste++, ans);
	}
	return 0;
}