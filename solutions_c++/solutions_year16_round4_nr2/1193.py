#include<stdio.h>

int n,m;
double p[20],tmpans;
int tmp[20],mem[20];
double ans;

void test(void)
{
	double pp=1;
	int i;
	for(i=1;i<=m;i++)
	{
		if(tmp[i]==1)
			pp*=p[mem[i]];
		else if(tmp[i]==2)
			pp*=(1-p[mem[i]]);
	}
	tmpans+=pp;
}


void recall(int A,int R,int lev)
{
	if(lev==m+1)
	{
		if(A==0 && R==0)
			test();
		return;
	}
	if(A!=0)
	{
		tmp[lev]=1;
		recall(A-1,R,lev+1);
	}
	if(R!=0)
	{
		tmp[lev]=2;
		recall(A,R-1,lev+1);
	}
	tmp[lev]=0;
}

void recall2(int M,int lev)
{
	if(lev==n+1)
	{
		if(M!=m)
			return;
		tmpans=0;
		recall(m/2,m/2,1);
		if(ans<tmpans)
			ans=tmpans;
		return;
	}
	mem[M+1]=lev;
	recall2(M+1,lev+1);
	mem[M+1]=0;
	recall2(M,lev+1);
}

void main(void)
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,i,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		ans=0.0;
		scanf("%d %d",&n,&m);
		for(j=1;j<=n;j++)
			scanf("%lf",&p[j]);
		recall2(0,1);
		printf("Case #%d: %.8lf\n",i,ans);
	}
}