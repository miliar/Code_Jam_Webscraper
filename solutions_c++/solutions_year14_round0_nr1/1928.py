#include<iostream>
#include<vector>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
	int r1,r2;
	vector<int> a1,a2,ans;
	int ar[5][5];
	cin>>r1;
	for(int j=1;j<5;j++)
	{
	 for(int k=1;k<5;k++)
	 {
	 	cin>>ar[j][k];
	 }
	}
	for(int j=1;j<=4;j++)
	{
		a1.push_back(ar[r1][j]);
	}
	cin>>r2;
	for(int j=1;j<5;j++)
	{
	 for(int k=1;k<5;k++)
	 {
	 	cin>>ar[j][k];
	 }
	}
	for(int j=1;j<=4;j++)
	{
		a2.push_back(ar[r2][j]);
	}
	for(int j=0;j<4;j++)
	{
		for(int k=0;k<4;k++)
		{
			if(a1[j]==a2[k])
			{
				ans.push_back(a1[j]);
			}
		}
	}
	cout<<"Case #"<<i<<": ";
	if(ans.size()==0)
	{
		cout<<"Volunteer cheated!\n";
	}
	if(ans.size()==1)
	{
		cout<<ans[0]<<endl;
	}
	if(ans.size()>1)
	{
		cout<<"Bad magician!"<<endl;
	}
}
return 0;
}
