#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int k, t;
	cin>>t;
	for(k=0;k<t;k++)
	{	
		vector<int> a1;
		vector<int> a2;
		int a[100][100], n, i, j;

		cin>>n;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			a1.push_back(a[n-1][i]);
		}
		cin>>n;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			a2.push_back(a[n-1][i]);
		}
		int count=0;
		int h;
	/*	for(i=0;i<4;i++)
			cout<<a1[i]<<" ";
		cout<<endl;
		for(i=0;i<4;i++)
			cout<<a2[i]<<" ";
		cout<<endl; */
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a1[i]==a2[j])
				{
					h=a1[i];
					count++;
					continue;
				}
			}
		}
//		cout<<count<<endl;
		if(count==1)
		{
			cout<<"Case #"<<k+1<<": "<<h<<endl;
		}
		else if(count==0)
		{
			cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!\n";
		}
		else if(count>1)
		{
			cout<<"Case #"<<k+1<<": "<<"Bad magician!\n";
		}
	}
}
