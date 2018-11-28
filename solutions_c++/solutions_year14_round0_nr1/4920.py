#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,r,i,l1,l2,x,ans,j=1;
	cin>>t;
	while(j<=t)
	{
		int a[17]={0},c=0;
		cin>>r;
		l1=4*(r-1)+1;
		l2=4*r+1;
		for(i=1;i<l1;i++)
		{
			cin>>x;
		}
		for(i=l1;i<l2;i++)
		{
			cin>>x;
			a[x]=1;
		}
		for(i=l2;i<=16;i++)
		{
			cin>>x;
		}
		cin>>r;
		l1=4*(r-1)+1;
		l2=4*r+1;
		for(i=1;i<l1;i++)
		{
			cin>>x;
		}
		for(i=l1;i<l2;i++)
		{
			cin>>x;
			if(a[x]==1){c++;ans=x;}
		}
		for(i=l2;i<=16;i++)
		{
			cin>>x;
		}
		if(c==1)printf("Case #%d: %d\n",j,ans);
		else if(c>1)printf("Case #%d: Bad magician!\n",j);
		else printf("Case #%d: Volunteer cheated!\n",j);
		j++;
	}
	return 0;
}

