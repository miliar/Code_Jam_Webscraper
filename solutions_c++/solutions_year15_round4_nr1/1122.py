#include<bits/stdc++.h>
using namespace std;
 
#define DEBUG //on-off switch for prlling statements
 
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
 
// Useful constants
#define INF                        (ll)1000000000
#define EPS                         1e-9
 
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(ll i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
 
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((ll)(a.size()))
 
// Some common useful functions
#define max(a,b)                     ( (a) > (b) ? (a) : (b))
#define min(a,b)                     ( (a) < (b) ? (a) : (b))
 
#define ll long long int
#define llu long long unsigned
#define ld long
 #define mod 1000000007
#define F first
#define S second
#define pb push_back
#define B 29
#define size1 340
#define llu long long unsigned
#define ld long
#define primemod 304250263527211
#define B 29
#define VI vector<int> 
#define mp make_pair
int mat[101][101];
int vis[101][101][4];
int r,c;
int flag=0;
int check(int x,int y)
{
	if(x < 0 || y <0 )return 0;
	if(x >= r || y>=c) return 0;
	return 1;
}
// left,right,up,down
void dfs(int x,int y,int dir)
{
	vis[x][y][dir] = 1;
	if(mat[x][y] != 0)
	dir=mat[x][y];
	if(dir == 1)
	{
		if(!check(x,y-1))
		{
			flag=1;
			return;
		}
		if(!vis[x][y-1][dir])
		dfs(x,y-1,dir);
	}
	else if(dir == 2)
	{
		if(!check(x,y+1))
		{
			flag=1;
			return;
		}
		if(!vis[x][y+1][dir])
		dfs(x,y+1,dir);
	}
	else if(dir == 3)
	{
		if(!check(x-1,y))
		{
			flag=1;
			return;
		}
		if(!vis[x-1][y][dir])
		dfs(x-1,y,dir);
	}
	else if(dir == 4)
	{
		if(!check(x+1,y))
		{
			flag=1;
			return;
		}
		if(!vis[x+1][y][dir])
		dfs(x+1,y,dir);
	}
}
	
	
void solve(int t)
{
	fill(mat,0);
	printf("Case #%d: ",t);
	string s;
	s(r);
	s(c);
	for(int i=0;i<r;i++)
	{
		cin >> s;
		for(int j=0;j<c;j++)
		{
			if(s[j] == '<')
			{
				mat[i][j] = 1;
			}
			else if(s[j] == '>')
			{
				mat[i][j] = 2;
			}
			else if(s[j] == '^')
			mat[i][j] = 3;
			else if(s[j] == 'v')
			mat[i][j] = 4;
		}
	}
	fill(vis,0);
	flag=0;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(mat[i][j] == 0)
			continue;
			if(!vis[i][j][mat[i][j]])
			dfs(i,j,mat[i][j]);
		}
	}
	if(flag == 0)
	{
		printf("0\n");
		return;
	}
	flag=0;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(mat[i][j] == 0)
			continue;
			int cnt=0;
			for(int k=0;k<r;k++)
			{
				if(k == i)
				continue;
				if(mat[k][j] != 0)
				cnt++;
			}
			for(int k=0;k<c;k++)
			{
				if(k == j)
				continue;
				if(mat[i][k] != 0)
				cnt++;
			}
			if(cnt == 0)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	int ans=0;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(mat[i][j] == 0)
			continue;
			flag=0;
			int dir=mat[i][j];
			if(dir == 1)
			{
				for(int k=j-1;k>=0;k--)
				{
					if(mat[i][k] != 0)
					flag++;
				}
				if(flag == 0)
				ans++;
			}
			else if(dir == 2)
			{
				for(int k=j+1;k<c;k++)
				{
					if(mat[i][k] != 0)
					flag++;
				}
				if(flag == 0)
				ans++;
			}
			else if(dir == 3)
			{
				for(int k=i-1;k>=0;k--)
				{
					if(mat[k][j] !=0)
					flag++;
				}
				if(flag ==0)
				ans++;
			}
			else if(dir == 4)
			{
				for(int k=i+1;k<r;k++)
				{
					if(mat[k][j]!=0)
					flag++;
				}
				if(flag == 0)
				ans++;
			}
		}
	}
	printf("%d\n",ans);
}
			
int main()
{

	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}
	