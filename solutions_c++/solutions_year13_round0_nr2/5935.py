#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<numeric>

using namespace std;

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("output4.txt","w",stdout);
	int m, n, t, ln[100][100];
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>m>>n;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				cin>>ln[i][j];
			}
		}
		int f=1;
		for(int i=0;i<m && f==1;i++)
		{
			for(int j=0;j<n;j++)
			{
				int p=1, q=1, p1=1,p2=1,q1=1,q2=1,r=1;
				for(int x=0;x<i;x++)
				{
					if(ln[x][j]>ln[i][j])
					{
						p1=0;
						break;
					}
				}
				for(int x=i+1;x<m;x++)
				{
					if(ln[x][j]>ln[i][j])
					{
						p2=0;
						break;
					}
				}
				if(i==0 || i==m-1)
				{
					if(p1==0 || p2==0)
					{
						p=0;
					}
				}
				else if(p1==0 && p2==0)
				{
					p=0;
					
				}
				for(int y=0;y<j;y++)
				{
					if(ln[i][y]>ln[i][j])
					{
						q1=0;
						break;
					}
				}
				for(int y=j+1;y<n;y++)
				{
					if(ln[i][y]>ln[i][j])
					{
						q2=0;
						break;
					}
				}
				if(j==0 || j==n-1)
				{
					if(q1==0 || q2==0)
					{
						q=0;
					}
				}
				else if(q1==0 && q2==0)
				{
					q=0;
					
				}
				if(ln[i][j]==2)
				{
					for(int x=0;x<m;x++)
					{
						for(int y=0;y<n;y++)
						{
							if(ln[x][y]==2 &&(ln[x][j]==1 || ln[i][y]==1))
							{
								r=0;
							}
						}
					}
				}
				
				if((p==0 && q==0) || r==0)
				{
					f=0;
					break;
				}
			}
		}
		if(f==1)
		{
			cout<<"Case #"<<k<<": YES"<<endl;
		}
		else
		{
			cout<<"Case #"<<k<<": NO"<<endl;
		}
	}
	return 0;
}
