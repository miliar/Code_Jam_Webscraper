#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("wow.out","w",stdout);
	int t,i,a,b,x,y,j;
	long long count;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		count=0;
		scanf("%d",&x);
		scanf("%1d",&b);
		for(i=1;i<=x;i++)
		{
		scanf("%1d",&a);
			if(i<=b)
			{
				b=a+b;
			}
			else
			{
				y=i-b;
				count+=y;
				b=a+y+b;
			}
		}
		printf("Case #%d: %Ld\n",j,count);
	}
	return 0;
}
