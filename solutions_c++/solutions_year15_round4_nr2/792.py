#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <cstring>
#include <cmath>
using namespace std;
double r[102],c[102];
int main()
{
	int t,n;
	double v,x,temp,temp2,v1,v2;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		scanf("%lf",&v);
		scanf("%lf",&x);
		printf("Case #%d: ",i);
		if(n==1)
		{
			scanf("%lf",&r[0]);
			scanf("%lf",&c[0]);
			if(c[0]!=x)
			{
				printf("IMPOSSIBLE\n");
			}
			else
			{
				temp = v/r[0];
				printf("%.7lf\n",temp);
			}
		}
		else
		{
			for(int j=0;j<n;j++)
			{
				scanf("%lf",&r[j]);
				scanf("%lf",&c[j]);
			}
			if(x<min(c[0],c[1])|| x>max(c[0],c[1]))
			{
				printf("IMPOSSIBLE\n");
			}
			else if(c[0]==c[1])
			{
				if(x!=c[0])
				{
					printf("IMPOSSIBLE\n");
				}
				else
				{
					r[0]=r[0]+r[1];
					temp = v/r[0];
					printf("%.7lf\n",temp);
				}
			}
			else
			{
				if(c[1]>c[0])
				{
					temp = c[1];
					c[1]=c[0];
					c[0]=temp;
					temp = r[0];
					r[0] = r[1];
					r[1] = temp;
				}
				v1 = x - c[1];
				temp = c[0] - c[1];
				v1 = v*v1;
				v1 = v1/temp;
				v2 = v - v1;
				temp = v1/r[0];
				temp2 = v2/r[1];
				if(temp<temp2)
				{
					temp = temp2;
				}
				printf("%.7lf\n",temp);
			}
		}
	}
	return 0;
}