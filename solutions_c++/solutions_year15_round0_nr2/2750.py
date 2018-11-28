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

int t, n, x, ans, teste = 1, tempo, maior;
int v[maxn];

int main()
{
	scanf("%d", &t);

	while(t--)
	{
		scanf("%d", &n);
		maior = 0;
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &v[i]);
			maior = max(maior, v[i]);
		}
		ans = inf;
		for(int j = 1; j <= maior; ++j)
		{
			tempo = j;
			for(int i = 0; i < n; ++i)
			{
				if(v[i] <= j) continue;
				tempo += (v[i]-1)/j;
			}
			ans = min(ans, tempo);
		}
		printf("Case #%d: %d\n", teste++, ans);
	}

	return 0;
}