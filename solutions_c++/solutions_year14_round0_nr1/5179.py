#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int ans1, ans2, mat1[4][4], mat2[4][4], count=0, ans;
		cin>>ans1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>mat1[j][k];
			}
		}
		cin>>ans2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>mat2[j][k];
			}
		}
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(mat1[ans1-1][j]==mat2[ans2-1][k])
				{
					count++;
					ans=mat1[ans1-1][j];
				}
			}
		}
		if(count==1)
		{
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
		if(count>1)
		{
			cout<<"Case #"<<i<<": Bad magician!\n";
		}
		if(count==0)
		{
			cout<<"Case #"<<i<<": Volunteer cheated!\n";
		}
	}
	return 0;
}
