#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		int s,c=0,p=0,d;
		char arr[1005];
		scanf("%d%s",&s,arr);
		c=(int)arr[0]-(int)'0';
		for(int i=1;i<=s;i++)
		{
			d=(int)arr[i]-(int)'0';
			if(d)
			{
				if(i>c)
				{
					p+=i-c;
					c=i;
					}
				c+=d;
				}
			}
		printf("Case #%d: %d\n",z,p);
		}
	
	return 0;
	}
