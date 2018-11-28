#include<iostream>
#include<cmath>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<bitset>
using namespace std;

int main()
{
     freopen("B-small-attempt0.in","r",stdin);
freopen("ou1t.txt","w",stdout);
int t,a,b,c,g;
scanf("%d",&t);
for(g=1;g<=t;g++)
{
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	int i,j,total=0;
	int m=max(a,b);
	int n=min(a,b);
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if((i&j)<c)
			total++;
		}
	}
	printf("Case #%d: %d\n",g,total);
		  }
return 0;
}
