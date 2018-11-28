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
	double *p=(double *)a;
	double *q=(double *)b;
	return p[0]-q[0];
}
int main()
{
	int t,test;
	si(test);
	for(t=1;t<=test;t++)
	{
		int n,i,j,l1=0,l2=0,r1,r2,ans1=0,ans2=0;
		double a[1002],b[1002];
		set<double> s;
		set <double>::iterator it;
		si(n);
		REP(i,n)
			scanf("%lf",&a[i]);
		REP(i,n)
		{
			scanf("%lf",&b[i]);
			s.insert(b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		r1=n-1;
		r2=n-1;
		REP(i,n)
		{
			if(a[l1]<b[l2])
			{
				l1++;
				r2--;
			}
			else if(a[l1]>b[l2] && a[r1]>b[r2])
			{
				ans1++;
				l1++;
				l2++;
			}
			else 
			{
				l1++;
				r2--;
			}
			it=s.upper_bound(a[i]);
			if(it!=s.end())
			{
				s.erase(it);
				ans2++;
			}
		}
		printf("Case #%d: %d %d\n",t,ans1,n-ans2);
	}
	return 0;
}
