#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <math.h>
#include <vector>
#include <ctime>
#include <cctype>
#include <stack>
#include <set>
#include <bitset>
#include <functional>
#include <numeric>
#include <stdexcept>
#include <utility> 
using namespace std;
#define ll long long 
#define m0(a) memset(a, 0, sizeof(a))
#define mf(a) memset(a, 0x7f, sizeof(a))
#define m1(a) memset(a, -1, sizeof(a))
#define C1(x)  cout<<x<<endl
#define C2(x,y)  cout<<x<<" "<<y<<endl
#define C3(x,y,z)  cout<<x<<" "<<y<<" "<<z<<endl
#define C4(x,y,z,zz)  cout<<x<<" "<<y<<" "<<z<<" "<<zz<<endl
#define min(x,y) ((x)>(y)?(y):(x))
#define max(x,y) ((x)>(y)?(x):(y))
#define r() (rand()/(double)(RAND_MAX))
struct stu
{
	int x,y,z;
	bool operator < (const stu &b) const
	{
		return x<b.x;	
	}
};
const int inf = 0x3f3f3f3f; 
const double eps = 1e-15;
const double pi = acos((double)-1) ;
const int maxn = 100100;
const ll M = 1e9+7;
int i,j,k,l,m,n,x,y,z,ans,num;
int a[maxn]={0};
int v[maxn]={0};
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
int b[20][4]={0};
int bb[20][4]={0};
int bbb[20][4]={0};
char cc[3]={'R','P','S'};
ll gcd(ll x,ll y)
{
	if (x==0 || y==0)  return x+y;
	return (x%y==0)?y:gcd(y,x%y);
}
long long extend_gcd(long long a,long long b,long long &x,long long &y)
{
    if(a==0&&b==0) return -1;
    if(b==0){x=1;y=0;return a;}
    long long d=extend_gcd(b,a%b,y,x);
    y-=a/b*x;
    return d;
}

long long mod_reverse(long long a,long long n)
{
    long long x,y;
    long long d=extend_gcd(a,n,x,y);
    if(d==1) return (x%n+n)%n;
    else return -1;
}

void dfs(int x,int y)
{
	if (y==0) {
		printf("%c",cc[x]);
		return ;
	}
	if (x==0)
	{
		if (y>1)
		{
			dfs(2,y-1);
			dfs(0,y-1);
		}
		else 
		{ 
			dfs(0,y-1);
			dfs(2,y-1);
		}
		
	}
	else if (x==1)
	{
		dfs(1,y-1);
		dfs(0,y-1);
		
	}
	else if(x==2)
	{
		if (y>2)
		{
			dfs(2,y-1);
			dfs(1,y-1);
			
			
		}
		else
		{
			dfs(1,y-1);
			dfs(2,y-1);
		}
		
	}
	
}
int main () 
{
	srand((unsigned)time(NULL));
	#ifdef ONLINE_JUDGE
	
	#else
	
	    freopen("A-small-attempt2.in","r",stdin);
	    freopen("in.out","w",stdout);
	
	#endif
	int cas;
	b[0][0]=1;
	for (int i=1;i<=15;i++)
	{
		b[i][0]=b[i-1][0]+b[i-1][1];
		b[i][1]=b[i-1][1]+b[i-1][2];
		b[i][2]=b[i-1][0]+b[i-1][2];
		
	}
	bb[0][1]=1;
	for (int i=1;i<=15;i++)
	{
		bb[i][0]=bb[i-1][0]+bb[i-1][1];
		bb[i][1]=bb[i-1][1]+bb[i-1][2];
		bb[i][2]=bb[i-1][0]+bb[i-1][2];
		//C3(bb[i][0],bb[i][1],bb[i][2]);
	}
	bbb[0][2]=1;
	for (int i=1;i<=15;i++)
	{
		bbb[i][0]=bbb[i-1][0]+bbb[i-1][1];
		bbb[i][1]=bbb[i-1][1]+bbb[i-1][2];
		bbb[i][2]=bbb[i-1][0]+bbb[i-1][2];
		//C3(bb[i][0],bb[i][1],bb[i][2]);
	}
	
	scanf("%d",&cas);
	for (int casi=1;casi<=cas;casi++)
	{
		scanf("%d%d%d%d",&n,&x,&y,&z);
		printf("Case #%d: ",casi);
		if (x==b[n][0] && y==b[n][1] && z==b[n][2])
		{
			dfs(0,n);
			printf("\n");
		}
		else if (x==bb[n][0] && y==bb[n][1] && z==bb[n][2])
		{
			
			dfs(1,n);
			printf("\n");
		}
		else if (x==bbb[n][0] && y==bbb[n][1] && z==bbb[n][2])
		{
			dfs(2,n);
			printf("\n");
		} 
		else
		{
			C1("IMPOSSIBLE");
		}
	}
	
	
	/*
	while (scanf("%d",&n)!=EOF)
	{
		if (n==0) break;
	}
	
	*/
	
	return 0;
}
