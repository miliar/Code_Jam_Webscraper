#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;



int main()
{


	freopen("A-small-attempt4.in","rt",stdin);
	freopen("A-small.out","wt",stdout);

	int i,t;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		int j,k,ans=0,flag=0,a1,a2;
		int a[4][4],b[4][4];
		
		cin>>a1;
		a1--;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>a[j][k];
			}
		}
		
		cin>>a2;
		a2--;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>b[j][k];
			}
		}
		
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[a1][j]==b[a2][k])
				{
					flag++;
					ans=a[a1][j];
					break;
				}
			}
		}
		
		if(flag==1)
			cout<<"Case #"<<i<<": "<<ans<<endl;
		if(flag>1)
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		if(flag==0)
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
	}
	
	return 0;
}
