#include <iostream>
#include <cstdio>
#include <string.h>
#include <cmath>
#include <algorithm>
using namespace std;

int a[8][8],b[8][8];

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	int t;
	int i,j,k,temp;
	int count,ans,ans1,ans2;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		count=0;
		cin>>ans1;
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				cin>>a[j][k];
			}
		}
		cin>>ans2;
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				cin>>b[j][k];
			}
		}
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				if(a[ans1][j]==b[ans2][k])
				{
					count++;
					ans=a[ans1][j];
				}
			}
		}
		if(count==1)
		{
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
		if(count==0)
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		if(count>1)
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
	}
	return 0;
}
