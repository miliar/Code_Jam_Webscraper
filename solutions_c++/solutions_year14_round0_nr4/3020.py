#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=1000+10;

double num1[maxn];
double num2[maxn];

int main ()
{
	freopen("D-large.txt","w",stdout);
	freopen("D-large.in","r",stdin);
	int t;
	while (scanf("%d",&t)==1)
	{
		for (int ii=1;ii<=t;ii++)
		{
			int n;
			int ans1=0,ans2=0;
			scanf("%d",&n);
			for (int i=0;i<n;i++)
			{scanf("%lf",&num1[i]);}
			for (int i=0;i<n;i++)
			{scanf("%lf",&num2[i]);}
			sort(num1,num1+n);
			sort(num2,num2+n);

			int p1=0,p2=0;
			ans1=n;
			while (p2<n)
			{
				if (num2[p2]<num1[p1])
				{p2++;}
				else
				{p1++;p2++;ans1--;}
			}

			p1=p2=0;
			while (p1<n)
			{
				if (num1[p1]<num2[p2])
				{p1++;}
				else
				{p1++;p2++;ans2++;}
			}

			printf("Case #%d: %d %d\n",ii,ans2,ans1);
		}
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}