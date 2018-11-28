#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
int t;
long long int a,b;
long long int pot10[10];
int conta(int v)
{
	int r=0;
	while(v>0)
	{
		v/=10;
		r++;
	}
	return r;
}
long long int contra(long long int v,int d)
{
	long long int r=0;
	for(int i=1;i<=d;i++)
	{
		long long int dig=v%10;
		r+=dig*pot10[d-i];
		v/=10;
	}
	return r;
}
vector<long long int> g; 
long long int bbin(int v)
{
	if(v==0) return 0;
	long long int ini=0;
	long long int fim=g.size()-1;
	while(ini<fim)
	{
		long long int m=(ini+fim)/2;
		if(g[m]>v)
		{
			fim=m;
		}
		else ini=m+1;
	}
	return fim;
}
int main()
{
	g.clear();
	g.push_back(1);
	g.push_back(4);
	g.push_back(9);
	pot10[0]=1;
	for(int i=1;i<10;i++) pot10[i]=10*pot10[i-1];
	for(long long int i=1;i<=10000000;i++)
	{
		int d=conta(i);
		long long int opa=contra(i,d);
		long long int p=i*pot10[d]+opa;
		long long int r=sqrt(p);
		int dr=conta(r);
		if(r*r==p && r==contra(r,dr))
		{
			//printf("%lld    %lld\n",r,p);
			g.push_back(p);
		}
		for(int j=0;j<=9;j++)
		{
			p=i*pot10[d+1]+j*pot10[d]+opa;
			r=sqrt(p);
			dr=conta(r);
			if(r*r==p && r==contra(r,dr))
			{
				//printf("%lld    %lld\n",r,p);
				g.push_back(p);
			}
		} 
	}
	sort(g.begin(),g.end());
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++)
	{
		scanf("%lld %lld",&a,&b);
		long long int pb=bbin(b);
		long long int pa=bbin(a-1);
		printf("Case #%d: ",caso);
		printf("%lld\n",pb-pa);
	}
	return 0;
}
