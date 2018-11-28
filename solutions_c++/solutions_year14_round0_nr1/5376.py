#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<functional>
#include<iostream>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define MP(a,b) make_pair(a,b)
#define clr(x,y) memset(x,y,sizeof x)
#define fi first
#define se second
#define sqr(z) ((z)*(z))
using namespace std;
typedef pair<int,int> PII;
const int oo=1047483647,maxn=110000;
int n,i,j,k,m,q,a[10][10],b[10][10],T;
bool v[20];
int main()
{
	freopen("1.in","r",stdin);
		freopen("1.out","w",stdout);
	scanf("%d",&T);
	int rt=0;
	for(;T;T--)
	{
		scanf("%d",&n);
		clr(v,0);
		fo(i,1,4)
		fo(j,1,4)
		{
			int x;
			scanf("%d",&x);
			if (i==n) v[x]=1; 
		}
		scanf("%d",&n);
		int ans=0;
		fo(i,1,4)
		fo(j,1,4)
		{
			int x;
			scanf("%d",&x);
			if ((i==n)&& v[x])
			{
				if (ans==0) ans=x;
				else ans=-1;
			}  
		}
		printf("Case #%d: ",++rt);
		if (ans==0) printf("Volunteer cheated!");
		else if (ans==-1) printf("Bad magician!");
		else printf("%d",ans);
		printf("\n");
	}
	return 0;
}
