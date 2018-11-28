/* 
    
      SHUBHAM RAI-IIIT Hyderabad
       
        */
#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<climits>
#include<string>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) for(i=0;i<a;i++)
#define LLD long long int
#define MOD 1000000007
#define si(n) scanf("%d",&n);
#define si2(n,m) scanf("%d%d",&n,&m);
#define sl(n) scanf("%lld",&n);
#define F first
#define S second
typedef pair<int,int> PII;
int compare(const void *a,const void *b)
{
	int * p=(int *)a;
	int *q=(int *)b;
	if(p[0]==q[0])
		return p[1]-q[1];
	return p[0]-q[0];
}
int main()
{
	int t,test;
	si(test);
	for(t=1;t<=test;t++)
	{
		double c,f,x,ans=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		double k1=x/c-2/f;
		int i,k=k1;
		for(i=0;i<k;i++)
			ans+=c/(2+i*f);
		if(k<0)
			k=0;
		ans+=x/(k*f+2);
		printf("Case #%d: %.7lf\n",t,ans);
	}
	return 0;
}
