#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<cstdlib>
#include<cctype>

#include<iostream>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<set>
#include<bitset>
#include<map>
#include<algorithm>

#define VI vector<int>
#define VD vector<double>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VII vector<PII >
#define VDD vector<PDD >
#define STI stack<int>
#define STD stack<double>
#define STII stack<PII >
#define STDD stack<PDD >

#define pb push_back
#define pf push_front
#define clr clear
#define res resize
#define ass assign
#define fir first
#define sec second

#define For(i,a,b) for(int i=a;i<=b;i++)
#define Dor(i,a,b) for(int i=a;i>=b;i--)
#define Fill(a,b) memset(a,b,sizeof(a))
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)

const int N=10010;
const int M=100010;
const double eps=1e-10;
const double dinf=1e10;
const int inf=1061109567;
const double Pi=3.14159265358;

using namespace std;

int mx[105],my[105];
int a[105][105];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T,cas=1;
	scanf("%d",&T);
	while (cas<=T)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		For(i,1,n) For(j,1,m) scanf("%d",&a[i][j]);
		For(i,1,n)
		{
			mx[i]=-1;
			For(j,1,m)
				if (mx[i]<a[i][j])
					mx[i]=a[i][j];
		}
		For(i,1,m)
		{
			my[i]=-1;
			For(j,1,n)
				if (my[i]<a[j][i])
					my[i]=a[j][i];
		}
		bool pass=1;
		For(i,1,n)
		{
			For(j,1,m)
				if (mx[i]==a[i][j]||my[j]==a[i][j])
					continue;
				else
				{
					pass=0;
					break;
				}
			if (!pass) break;
		}
		printf("Case #%d: ",cas);
		if (pass) printf("YES\n");
		else printf("NO\n");
		cas++;
	}
	return 0;
}
