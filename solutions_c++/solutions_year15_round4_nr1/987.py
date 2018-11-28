#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef unsigned long long ull;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second

 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};	
//////////////////////

const int N = 101;

int n,m;
char v[N][N];
int vis[N][N];
int ans;

bool in_range( int x, int y ){ return (x>=0 && x<n && y>=0 && y<m); }

int dir( char c )
{
	if( c == 'v' ) return 0;
	if( c == '^' ) return 1;
	if( c == '<' ) return 2;
	if( c == '>' ) return 3;
}


void main2()
{	
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;++i) for(int j=0;j<m;++j) scanf(" %c",&v[i][j]); 
	ans = 0;
	for(int i=0;i<n && ans>=0;++i)
	{
		for(int j=0;j<m && ans>=0;++j)
		{
			if( v[i][j] == '.' ) continue;
			int d = dir(v[i][j]);
			int ok = 0;
			int xx = i, yy = j;
			while(1)
			{
				xx += dx[d];
				yy += dy[d];
				if( !in_range(xx,yy) ) break;
				if( v[xx][yy] != '.' )
				{
					ok = 1;
					break;
				}
			}			
			if( !ok )
			{
				ans++;
				for(int d=0;d<4;++d)
				{
					xx = i;
					yy = j;
					while(1)
					{
						xx += dx[d];
						yy += dy[d];
						if( !in_range(xx,yy) ) break;
						if( v[xx][yy] != '.' )
						{
							ok = 1;
							break;
						}
					}	
				}
				if( !ok ) ans = -INF;
			}
		}
	}
	if( ans < 0 ) printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);
}

int main()
{
	//ios::sync_with_stdio(0);
	int tt; scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		printf("Case #%d: ",t);
		main2();
	}
	return 0;
}	