#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<queue>
using namespace std;
#define inp(a) scanf("%lld",&a)
#define line(a) printf("%lld ",a);
#define next() printf("\n");
#define out(a) printf("%lld\n",a)
#define swap(a,b) {a=a+b;a=a-b;b=a-b;}
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define ll long long int
#define mod 1000000007
#define getcx getchar_unlocked
/*inline void fscan(ll *a )
{
	ll n=0; int ch = getcx(); int sign = 1;
	while(ch < '0' || ch > '9')
	{
	if(ch == '-') sign=-1; ch = getcx();
	}
	while(ch >= '0' && ch <= '9')
	{
	n = (n << 3) + (n << 1) + ch - '0', ch = getcx();
	}
	*a = n * sign;
}*/
double c,f,x,cost[10000];
		
int t;
int main()
{
	int l;
	scanf("%d",&t);
	for(l=1;l<=t;l++)
	{
		int i;
		scanf("%lf %lf %lf",&c,&f,&x);
		cost[0]=x/2;
		double ini=c/2;
		double a=2;
		for(i=1;;i++)
		{
			cost[i]=ini;
			double b=a+f,sum=0;
			for(int j=1;j<=i-1;j++)
			{
				sum=sum+c/b;
				b=b+f;
			}
			sum=sum+x/b;
			cost[i]+=sum;
			
			if(cost[i]>=cost[i-1])
			break;
		}
		printf("Case #%d: %.7lf\n",l,cost[i-1]);
	}
	return 0;
}

