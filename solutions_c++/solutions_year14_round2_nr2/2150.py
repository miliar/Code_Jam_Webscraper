#include<iostream>
#include<string>
#include<cmath>
#include<conio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<stack>
#include<cctype>
#include<cmath>
#include<cstring>
#include<queue>
#include<cstdio>
#include<sstream>
#include<bitset>
using namespace std;
#define pb push_back
#define pi 3.141592653589793238462643383

int main()
{   freopen("B-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
int t,a,b,c,k;
scanf("%d",&t);
for(k=1;k<=t;k++)
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
	printf("Case #%d: %d\n",k,total);
		  }
getch();
return 0;
}
	      
	      
		   
