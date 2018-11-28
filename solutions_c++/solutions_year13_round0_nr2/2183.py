#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<sstream>
#include<math.h>
using namespace std;
bool check(vector<vector<int> >& grid)
{
	vector<vector<int> > temp_grid;
	vector<int>temp;
	for(int j=0;j<grid.size();j++)
	{
		temp_grid.push_back(temp);
		for(int k=0;k<grid[0].size();k++)
		{
			temp_grid[j].push_back(100);
		}
	}
	for(int i=0;i<grid.size();i++)
	{
		int maxi=0;
		for(int k=0;k<grid[0].size();k++)
		{
			maxi=max(maxi,grid[i][k]);
		}
		for(int k=0;k<grid[0].size();k++)
		{
			temp_grid[i][k]=min(temp_grid[i][k],maxi);
		}
	}
	for(int i=0;i<grid[0].size();i++)
	{
		int maxi=0;
		for(int k=0;k<grid.size();k++)
		{
				maxi=max(maxi,grid[k][i]);
		}
		for(int k=0;k<grid.size();k++)
		{
			temp_grid[k][i]=min(temp_grid[k][i],maxi);
		}
	}
	for(int j=0;j<grid.size();j++)
		{
			for(int k=0;k<grid[0].size();k++)
			{
				if(grid[j][k]!=temp_grid[j][k]) return false;
			}
		}
	return true;
}
int main()
{
	int t,m,n,x;
	ifstream cin;
	ofstream cout;
	cin.open("B-large.in");
	cout.open("outputprob2large.txt");
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>m;
		vector<vector<int> > grid;
		vector<int>temp;
		for(int j=0;j<n;j++){
			grid.push_back(temp);
			for(int k=0;k<m;k++)
			{
				cin>>x;
				grid[j].push_back(x);
			}
		}
		bool c = check(grid);
		cout<<"Case #"<<i+1<<": ";
		if(c) cout<<"YES"<<endl;
		else  cout<<"NO"<<endl;
	}
}
