#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 1000+10
int war, dwar,N,av[maxn],bv[maxn];
double a[maxn],b[maxn];
int cmp(double x)
{
	for(int i=0;i<N;i++)
	{
		if(!bv[i] && b[i]>x)
			{bv[i]=1;return 0;}
	}
	for(int i=0;i<N;i++)
		if(!bv[i])
		{
			bv[i]=1;return 1;
		}
}
int dcmp(double x)
{
	for(int i=0;i<N;i++)
	{
		if(!av[i] && a[i]>x) {av[i]=1;return 1;}
	}
	for(int i=0;i<N;i++)
		if(av[i])
		{
			av[i]=1;return 0;
		}
}
int main(void)
{
	freopen("C:\\Users\\ytimex\\Desktop\\gcj\\D-small-attempt0.in","rb",stdin);
	freopen("C:\\Users\\ytimex\\Desktop\\gcj\\D-small-attempt0.out","wb",stdout);
	int T,t=1;
	scanf("%d",&T);
	while(t <= T)
	{
		war=0, dwar=0;
		scanf("%d",&N);
		memset(av,0,sizeof(av));
		memset(bv,0,sizeof(bv));
		for(int i=0;i<N;i++)
			scanf("%lf",&a[i]);
		for(int i=0;i<N;i++)
			scanf("%lf",&b[i]);
		sort(a,a+N); sort(b,b+N);
		for(int i=0;i<N;i++)
		{
			war += cmp(a[i]);
			av[i] = 1;
		}
		memset(av,0,sizeof(av));
		memset(bv,0,sizeof(bv));
		for(int i=0;i<N;i++)
		{
			dwar += dcmp(b[i]);
			bv[i] = 1;
		}
		printf("Case #%d: %d %d\n",t,dwar,war);
		t++;
	}
	return 0;
}
