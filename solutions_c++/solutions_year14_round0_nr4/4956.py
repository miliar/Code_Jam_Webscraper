#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int main() 
{
	int t,n,i,ans1,ans2,k,a,b;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		ans1=0;
		ans2=0;
		scanf("%d",&n);
		vector <float> na(n),ken(n);
		for(i=0;i<n;i++)
		scanf("%f",&na[i]);
		for(i=0;i<n;i++)
		scanf("%f",&ken[i]);
		sort(na.begin(),na.end());
		sort(ken.begin(),ken.end());
		a=0;
		b=0;
		while(1)
		{
			if(ken[b]<na[a])
			{
				ans1++;	a++;	b++;
			}
			else	a++;
			if(a==n||b==n)	break;
		}
		a=0;
		b=0;
		while(1)
		{
			if(ken[b]>na[a])
			{
				ans2++;	a++;	b++;
			}
			else	b++;
			if(a==n||b==n)	break;
		}
		printf("Case #%d: %d %d\n",k,ans1,n-ans2);
		na.clear();
		ken.clear();
	}
	return 0;
}