#include <iostream>
#include <algorithm>

using namespace std;

int t;
int n, m;

int pattern[100][100];
int max_row[100];
int max_col[100];

int lawn[100][100];
int max_row_l[100];
int max_col_l[100];

void cut_col(int col, int val)
{
	for(int i=0; i<n; i++)
		lawn[i][col]=min(val, lawn[i][col]);
}
void cut_row(int row, int val)
{
	for(int i=0; i<m; i++)
		lawn[row][i]=min(val, lawn[row][i]);
}
bool cut()
{
	for(int i=0; i<n; i++)
	{
		if(max_row[i]<max_row_l[i])
		{
			cut_row(i, max_row[i]);
			max_row_l[i]=max_row[i];
			return true;
		}
	}
	for(int i=0; i<m; i++)
	{
		if(max_col[i]<max_col_l[i])
		{
			cut_col(i, max_col[i]);
			max_col_l[i]=max_col[i];
			return true;
		}
	}
	return false;
}
bool match()
{
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(pattern[i][j]!=lawn[i][j])
				return false;
		}
	}
	return true;
}

int main()
{
	cin>>t;
	int k=1;
	while(k<=t)
	{
		cin>>n>>m;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				cin>>pattern[i][j];
				lawn[i][j]=1000;
			}
		}

		for(int i=0; i<n; i++)
		{
			max_row[i]=0;
			max_row_l[i]=1000;
		}
		for(int i=0; i<m; i++)
		{
			max_col[i]=0;
			max_col_l[i]=1000;
		}
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
				max_row[i]=max(max_row[i], pattern[i][j]);			
		}
		for(int i=0; i<m; i++)
		{
			for(int j=0; j<n; j++)
				max_col[i]=max(max_col[i], pattern[j][i]);
		}
		while(cut()==true)
		{ }
		
		if(match()==true)
		{
			cout<<"Case #"<<k<<": YES\n";
		}
		else
		{
			cout<<"Case #"<<k<<": NO\n";
		}
		k++;
	}
	return 0;
}
