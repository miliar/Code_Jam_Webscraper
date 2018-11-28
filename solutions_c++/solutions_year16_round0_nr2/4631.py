#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int i;
	int j;
	for(i=1;i<=t;i++)
	{
		string a;
		int cnt=0;
		cin>>a;
		int lm=a.size();
		for(j=0;j<lm-1;j++)
		{
			if(a[j]!=a[j+1])
				cnt++;
		}
		if(a[lm-1]=='-')
		cnt++;
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}
