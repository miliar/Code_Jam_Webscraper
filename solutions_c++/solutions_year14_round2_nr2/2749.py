#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<set>
using namespace std;

int main()
{
	int test,t,a,b,k,i,j,ans;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		ans=0;
		scanf("%d%d%d",&a,&b,&k);
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}