#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#define mod 1000000009
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,m,i,j,k,count,flag;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		int a[5][5],b[5][5],c[17];
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>a[i][j];
			}
		}
		memset(c,0,sizeof(c));
		for(j=1;j<=4;j++)
		{
				c[a[n][j]]++;
		}
		cin>>m;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>b[i][j];
			}
		}
		count=0;
		for(j=1;j<=4;j++)
		{
			if(c[b[m][j]]==1)
			{
				count++;
				flag=b[m][j];
				c[b[m][j]]++;
			}
		}
		if(count==1)
		{
			cout<<"Case #"<<k<<": "<<flag<<endl;
		}
		else if(count==0)
		{
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		}
	}
	return 0;
}
