#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int a[4][4];
		int b[4][4];
		int row1,row2;
		cin>>row1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>row2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		vector<int> f;
		vector<int> s;
	row1--;
	row2--;
	for(int i=0;i<4;i++)
	{
		f.push_back(a[row1][i]);
	}
	for(int i=0;i<4;i++)
	{
		s.push_back(b[row2][i]);
	}
	int count = 0;
	int ans = 0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(f[i]==s[j])
			{
				ans = f[i];
				count++;
				break;

			}	
		}
	}
	if(count==0)
	{
		cout<<"Case #"<<k+1<<":"<<" "<<"Volunteer cheated!"<<endl;
	}
	else if(count==1)
	{
		
	
		cout<<"Case #"<<k+1<<":"<<" "<<ans<<endl;
	}
	
	else
	{
		
	
		cout<<"Case #"<<k+1<<":"<<" "<<"Bad magician!"<<endl;
		
	}
	
	}

	cin>>t;
	return 0;
}