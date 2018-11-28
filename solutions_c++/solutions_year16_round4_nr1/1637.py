#include <cstdio>

using namespace std;

int rsp[5000];
int co[5000];
int n;

bool check(int curn)
{
	int i;
	curn/=2;
	if(curn==0)
		return true;

	for(i=0;i<curn;i++)
	{
		if(co[2*i]==co[2*i+1])
			return false;
		if(co[2*i]==0)
		{
			if(co[2*i+1]==1)
				co[i]=1;
			else
				co[i]=0;
		}
		else if(co[2*i]==1)
		{
			if(co[2*i+1]==0)
				co[i]=1;
			else
				co[i]=2;
		}
		else
		{
			if(co[2*i+1]==0)
				co[i]=0;
			else
				co[i]=2;
		}
	}

	return check(curn);
}

bool assign(int cur,int r,int p, int s)
{
	int i;

	if(cur==n)
	{
		for(i=0;i<n;i++)
			co[i]=rsp[i];
		if(check(n))
			return true;
		else
			return false;
	}
	
	if(p!=0)
	{
		rsp[cur]=1;
		if(assign(cur+1,r,p-1,s))
			return true;
	}

	if(r!=0)
	{
		rsp[cur]=0;
		if(assign(cur+1,r-1,p,s))
			return true;
	}

	if(s!=0)
	{
		rsp[cur]=2;
		if(assign(cur+1,r,p,s-1))
			return true;
	}

	return false;
}

int main()
{
	int t,T,r,p,s,i,tmp;

	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d %d %d",&n,&r,&p,&s);
		n=r+p+s;
		printf("Case #%d: ",t);
		if(assign(0,r,p,s))
		{
			for(i=0;i<n;i++)
				if(rsp[i]==0)
					putchar('R');
				else if(rsp[i]==1)
					putchar('P');
				else
					putchar('S');
		}
		else
			printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
