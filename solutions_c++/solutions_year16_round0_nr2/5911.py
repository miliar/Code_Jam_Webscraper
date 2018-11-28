/*
author:arushi
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,x=0;
	scanf("%d",&t);
	while(t--)
	{
		x++;
		int count=0;
		string a;
		cin>>a;
		for(int i=(int)a.size()-1;i>=0;i--)
		{
			if(count%2!=0)
			{
				if(a[i]=='-')
					a[i]='+';
				else
					a[i]='-';
			}
			if(a[i]=='-')
				count++;
		}
		printf("Case #%d: %d\n",x,count);
	}
	return 0;
}