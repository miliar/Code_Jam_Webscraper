#include <cstdio>
#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string.h>
#define lldd long long int
using namespace std;
int main()
{
freopen("A-a-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
int t;
scanf("%d",&t);
for(int q=1;q<=t;q++)
	{
		lldd a,b,k;
		scanf("%lld %lld %lld",&a,&b,&k);
			lldd count=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				lldd c=i&j;
				if(c<k)
				  count++;
			}
			
		}
		printf("Case #%d: %lld\n",q,count);
	}
return 0;	
}