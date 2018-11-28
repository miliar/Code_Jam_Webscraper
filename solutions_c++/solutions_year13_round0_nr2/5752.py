#include<iostream>
#include<math.h>
#include<string>
#include<string.h>
#include<sstream>
#include<algorithm>
#include<vector>
using namespace std;
int a[100][100],n,m,t=0;
int map(int x,int y,int mini)
{
	int i,j,r=0,u=0;
	for(i=0;i<m;i++)
	{
		if(a[x][i]==mini)
			r++;
	}
	for(i=0;i<n;i++)
	{
		if(a[i][y]==mini)
			u++;
	}
	if(r==m || u==n)
		return 1;
	else
		return 0;
}
			
int main()
{
	int ch,i,j,z=0,min;
	freopen("B-small-attempt4.in","rt",stdin);
	freopen("B.out","wt",stdout);
	cin>>ch;
	while(ch>0)
	{
	cin>>n>>m;
	z=-1;min=101;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			cin>>a[i][j];
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(min>a[i][j])
			min=a[i][j];
		
		}
	}
	try
	{
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			if(a[i][j]==min)
			{	
				z=map(i,j,min);			
				if(z==0)
					throw z;			
			}
		}
	}
	}
	
	
	catch(int p)
	{}
	t++,ch--;
	if(z==1)
	{
		cout<<"Case #"<<t<<": "<<"YES"<<endl;
	}
	else
	{
		cout<<"Case #"<<t<<": "<<"NO"<<endl;
	}
	}
	return 0;
}
