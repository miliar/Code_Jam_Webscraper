#include<iostream>
#include<vector>
#include<algorithm>
int a[10][10];
using namespace std;
int main()
{
	int n,m;
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{

	cin>>n>>m;
	vector<int> row(n,0);
	vector<int> col(m,0);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cin>>a[i][j];
			if(a[i][j]==1)
			{
				row[i]++;
				col[j]++;
			}
		}
	}		
	bool flag=false;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(a[i][j]==1)
			{
				if(row[i]!=m&&col[j]!=n)
				{
					cout<<"Case #"<<test+1<<":"<<" "<<"NO"<<endl;
					flag = true;
					break;
				}
			}
		}
		if(flag==true)
				break;
	}
	if(flag==false)
		cout<<"Case #"<<test+1<<":"<<" "<<"YES"<<endl;
	}
	return 0;
}