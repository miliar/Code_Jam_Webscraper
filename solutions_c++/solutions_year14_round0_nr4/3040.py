#include <stdio.h>
#include <algorithm>
using namespace std;
const int MAXN=1010;
double na[MAXN];
double k[MAXN];
int marc[MAXN];

int main()
{
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&na[i]);
		}
		sort(&na[0],&na[n]);	
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&k[i]);
		}
		sort(&k[0],&k[n]);	
		
		int r1=0;
		for(int i=0;i<n;i++) marc[i]=0;
		int cur=0;
		for(int i=0;i<n && cur<n;i++)
		{
			while(cur<n && na[cur]<k[i]) cur++;
			if(cur==n) break;
			r1++;
			cur++;
		}
		
		int r2=0;
		cur=0;
		for(int i=0;i<n && cur<n;i++)
		{
			while(cur<n && k[cur]<na[i]) cur++;
			if(cur==n) break;
			r2++;
			cur++;
		}
		r2=n-r2;
		printf("Case #%d: %d %d\n",ti,r1,r2);
	}
	return 0;	
}
