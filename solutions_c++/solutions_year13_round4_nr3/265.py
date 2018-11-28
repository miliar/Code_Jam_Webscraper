#include <cstdio>

int n;
int a[2005];
int b[2005];

int zap[2005];
bool ok[2005];
int pop[2005];
int nas[2005];

int l[2005];

void ustawa(int p,int x)
{
	int o= -1;
	for(int i=p;i<n;i++)
	{
		if(!ok[i] && a[i]==x)
		{
			pop[i]=o;
			o=i;
		}
	}
	if(o>=0) zap[o]|=1;
}

void ustawb(int p,int x)
{
	int o= -1;
	for(int i=p;i>=0;i--)
	{
		if(!ok[i] && b[i]==x)
		{
			nas[i]=o;
			o=i;
		}
	}
	if(o>=0) zap[o]|=2;
}

void przyp()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++) scanf("%d",a+i);
	for(int i=0;i<n;i++) scanf("%d",b+i);
	for(int i=0;i<n;i++) ok[i]=false;
	for(int i=0;i<n;i++) zap[i]=0,pop[i]=nas[i]= -1;
	ustawa(0,1);
	ustawb(n-1,1);
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(!ok[j] && zap[j]==3)
			{
				l[j]=i;
				ustawa(j+1,a[j]+1);
				ustawb(j-1,b[j]+1);
				if(nas[j]>=0) zap[nas[j]]|=2;
				if(pop[j]>=0) zap[pop[j]]|=1;
				ok[j]=true;
				break;
			}
		}
	}
	for(int i=0;i<n;i++) printf("%d ",l[i]);
	printf("\n");
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) printf("Case #%d: ",i),przyp();
	return 0;
}
