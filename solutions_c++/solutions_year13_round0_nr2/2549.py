#include<iostream>
#include<map>
#include<string.h>
using namespace std;
int arr[101][101];
int r[101],c[101];
bool mark[101][101];
int main()
{
	int tc;
	cin>>tc;
	int cc=0;
	while(tc--)
	{
		++cc;
		memset(mark,0,sizeof mark);
		for(int i=0 ; i<101 ; ++i)
		{
			r[i]=-1,c[i]=-1;
		}
		int n,m;
		cin>>n>>m;
		for(int i=0 ; i<n ; ++i)
		for(int j=0 ; j<m ; ++j)
		cin>>arr[i][j];
		int mx=-1;
		for(int i=0 ; i<n ; ++i)
		{
			int ii=-1,jj=-1;
			mx=-1;
			for(int j=0 ; j<m ; ++j)
			{
				if(arr[i][j]>mx)
				{
					mx=arr[i][j];
					ii=i,jj=j;
				}
			}
			r[ii]=jj;
		}
		mx=-1;
		for(int j=0 ; j<m ; ++j)
		{
			int ii=-1,jj=-1;
			mx=-1;
			for(int i=0 ; i<n ; ++i)
			{
				if(arr[i][j]>mx)
				{
					mx=arr[i][j];
					ii=i,jj=j;
				}
			}
			c[jj]=ii;
		}
		for(int i=0 ; i<n ; ++i)
		{
			int a=arr[i][r[i]];
			for(int j=0 ; j<m ; ++j)
			{
				if(arr[i][j]==a)
				mark[i][j]=1;
			}
		}
		for(int j=0 ; j<m ; ++j)
		{
			int a=arr[c[j]][j];
			for(int i=0 ; i<n ; ++i)
			{
				if(arr[i][j]==a)
				mark[i][j]=1;
			}
		}
		bool is=1;
		for(int i=0 ; i<n ; ++i)
		for(int j=0 ; j<m ; ++j)
		if(!mark[i][j])
		{
			is=0;
			break;
		}
		cout<<"Case #"<<cc<<": ";
		if(is)
		cout<<"YES"<<endl;
		else
		cout<<"NO"<<endl;
	}
}
