#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
#define re(i,s,t) for(int i=s;i<=t;i++)

int t;
double c,f,x,ans;

void work(int u)
{
	double hen=2;
    ans=0;
	re(i,1,u)
	{
		ans+=(double)c/hen;
		hen+=f;
	}
	ans+=(double)x/hen;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);int tt=0;
	while(t--)
	{
		tt++;
		//scanf("%lf %lf %lf",c,f,x);
		cin >>c>>f>>x;
	    double min=~0u>>2; 
		re(i,0,x/c)
		{
			work(i);
			if(ans<min)min=ans;
		}
		printf("Case #%d: %.7lf\n",tt,min);
	}
	return 0;
}
