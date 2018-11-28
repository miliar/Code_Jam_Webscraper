#include <bits/stdc++.h>

#define maxn 111
#define logn 23
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

int t, teste = 1;
int r, c;
char m[maxn][maxn];
int ok;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
// v > ^ <
int main()
{
	int xx, yy, ans;
	scanf("%d", &t);

	while(t--)
	{
		ans = 0;
		ok = 1;
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				scanf(" %c", &m[i][j]);
			}
		}

		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if(m[i][j] == '.') continue;
				int aux = 0, dir;
				if(m[i][j] == 'v') dir = 0;
				else if(m[i][j] == '>') dir = 1;
				else if(m[i][j] == '^') dir = 2;
				else if(m[i][j] == '<') dir = 3;

				xx = i;
				yy = j;
				while(1)
				{
					xx += dx[dir];
					yy += dy[dir];

					if(!(xx >= 0 && xx < r && yy >= 0 && yy < c))
						break;

					if(m[xx][yy] != '.')
					{
						aux = 1;
						break;
					}
				}
				if(aux) continue;

				for(int k = 0; k < 4; ++k)
				{
					if(aux) break;
					if(k == dir) continue;
					xx = i;
					yy = j;

					while(1)
					{
						xx += dx[k];
						yy += dy[k];

						if(!(xx >= 0 && xx < r && yy >= 0 && yy < c))
							break;

						if(m[xx][yy] != '.')
						{
							aux = 1;
							break;
						}
					}
				}
				if(aux) ans++;
				else ok = 0;
			}
		}

		if(!ok) printf("Case #%d: IMPOSSIBLE\n", teste++);
		else printf("Case #%d: %d\n", teste++, ans);
	}

	return 0;
}