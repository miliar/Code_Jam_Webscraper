#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<iostream>
#include<cmath>
#include<cctype>
#include<ctime>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<queue>
#include<vector>
#include<deque>
#include<complex>
using namespace std;
#define For(i,n) for(int i=1;i<=n;i++)
#define Fork(i,k,n) for(int i=k;i<=n;i++)
#define Rep(i,n) for(int i=0;i<n;i++)
#define ForD(i,n) for(int i=n;i;i--)
#define RepD(i,n) for(int i=n;i>=0;i--)
#define Forp(x) for(int p=pre[x];p;p=next[p])
#define Forpiter(x) for(int &p=iter[x];p;p=next[p])  
#define Lson (x<<1)
#define Rson ((x<<1)+1)
#define MEM(a) memset(a,0,sizeof(a));
#define MEMI(a) memset(a,127,sizeof(a));
#define MEMi(a) memset(a,128,sizeof(a));
#define INF (2139062143)
#define F (100000007)
#define MAXN (100+10)
#define MAXT (100+10)
typedef long long ll;
ll mul(ll a,ll b){return (a*b)%F;}
ll add(ll a,ll b){return (a+b)%F;}
ll sub(ll a,ll b){return (a-b+(a-b)/F*F+F)%F;}
void upd(ll &a,ll b){a=(a%F+b%F)%F;}
char c[MAXN][MAXN];
int a[MAXN][MAXN];
bool b[MAXN][MAXN];
int n,m;
int h[MAXN];
bool is_ok()
{
	For(i,n)
	{
		For(j,m)
			if (a[i][j])
			{
				int p=0;
				For(k,m) if(a[i][k]) ++p;
				For(k,n) if(a[k][j]) ++p;
				if (p==2) return 0;
			}
	}
	return 1;
		
}
bool insi(int i,int j)
{
	return 1<=i&&i<=n&&1<=j&&j<=m;
}
int dir[5][3]={{},{0,-1,0},{0,1,0},{0,0,-1},{0,0,1}}; 
int dfs(int i,int j,int di,int fi,int fj)
{
	if (!(i==fi&&j==fj))
	{
		if (b[i][j]) return 0;
		
		if (!insi(i,j)) return 1;
	}
	if (a[i][j]) b[i][j]=1,di=a[i][j];	
	
	dfs(i+dir[di][1],j+dir[di][2],di,fi,fj);
}
int main()
{
	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	
	h['.']=0,h['^']=1,h['v']=2,h['<']=3,h['>']=4;
	
	int T;
	cin>>T;
	For(kcase,T)
	{
		cin>>n>>m;
		MEM(b)
		For(i,n) scanf("%s",c[i]+1);
		
		For(i,n) 
		{
			For(j,m)
				a[i][j]=h[c[i][j]];
		}
		
		if (!is_ok())
		{
			printf("Case #%d: IMPOSSIBLE\n",kcase);
			continue;
		}
		
		ll ans=0;

		For(i,n)
			For(j,m)
				if (a[i][j]&&!b[i][j])
				{
					ans+=dfs(i,j,a[i][j],i,j);
					
				} 



		printf("Case #%d: %lld\n",kcase,ans);
	}

	
	return 0;
}

