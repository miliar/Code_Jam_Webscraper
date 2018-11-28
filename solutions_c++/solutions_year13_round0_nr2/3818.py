#include<iostream>

using namespace std;

int mower[100][100],row,col;

int check_row(int n,int m)
{
	int i;
	for(i=0;i<col;i++)
		if(mower[n][m]<mower[n][i])
			return 0;

	return 1;
}

int check_col(int n,int m)
{
	int i;
	for(i=0;i<row;i++)
		if(mower[n][m]<mower[i][m])
			return 0;

	return 1;
}

int main()
{
	int t,i,j,run=1,broke,ans[101];
	cin>>t;
	while(run<=t)
	{
		cin>>row;
		cin>>col;
		for(i=0;i<row;i++)
			for(j=0;j<col;j++)
				cin>>mower[i][j];
		broke=0;
		for(i=0;i<row;i++)
		{
			for(j=0;j<col;j++)
				if( !(check_row(i,j) || check_col(i,j)) )
				{
					ans[run]=0;
					broke=1;
					break;
				}
			if(broke==1)
				break;
		}
		if(broke==0)
			ans[run]=1;
		run++;
	}

	for(i=1;i<t+1;i++)
		{
			if(ans[i]==0)
				cout<<"Case #"<<i<<": "<<"NO"<<"\n";
			else if(ans[i]==1)
				cout<<"Case #"<<i<<": "<<"YES"<<"\n";
		}

}