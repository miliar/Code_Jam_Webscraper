#include <math.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
int s[100][100];
int s1[100][100];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
  int t,n,m;
	cin>>t;
	for(int i1=0;i1<t;i1++)
	{   int a=1;
		for(int i=0;i<100;i++)
		{
			for(int j=0;j<100;j++)
			{
			s[i][j]=0;
			s1[i][j]=0;
			}
		}
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{	int d;
				cin>>d;
				s[i][j]=d;
				s1[i][j]=1000;
			}
		}
		for(int i=0;i<n;i++)
		{
			int l=1;
			for(int j=0;j<m;j++)
			{
				if(s[i][j]>l) l=s[i][j];
			}
			for(int j=0;j<m;j++)
			{
				s1[i][j]=min(s1[i][j], l);
			}
		}
		for(int j=0;j<m;j++)
		{
			int l=1;
			for(int i=0;i<n;i++)
			{
				if(s[i][j]>l) l=s[i][j];
			}
			for(int i=0;i<n;i++)
			{
				s1[i][j]=min(s1[i][j], l);
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(s1[i][j]!=s[i][j])
				{
					a=0;
				}
			}
		}
	 if (a==1) cout<<"Case #"<<i1+1<<": "<<"YES"<<endl;
	 else cout<<"Case #"<<i1+1<<": "<<"NO"<<endl;

	}
return 0;
}
