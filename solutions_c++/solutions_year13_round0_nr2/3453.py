#include<iostream>

using namespace std;

int fun(int n, int m)
{
		int ar[100][100],temp[100][100];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				temp[i][j]=100;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				cin>>ar[i][j];
		}
		for(int i=0;i<m;i++)
		{
			int a=-1;  //=findmax(i);
			for(int x=0;x<n;x++)
			{
				if(a<ar[x][i])
					a=ar[x][i];
			}
			//changecol(i,a);
			for(int x=0;x<n;x++)
			{
				if(temp[x][i]>a)
					temp[x][i]=a;
			}
			for(int j=0;j<n;j++)
			{
				if(ar[j][i]!=temp[j][i])
				{
					if(temp[j][i]<ar[j][i])
						return 0;
					//changerow(j,ar[j][i]);
					for(int x=0;x<m;x++)
					{
						if(temp[j][x]>ar[j][i])
							temp[j][x]=ar[j][i];
					}
				}
				for(int k=i-1;k>=0;k--)
				{
					if(ar[j][k]!=temp[j][k])
					{
						return 0;
					}
				}
			}
		}
		return 1;
}

int main()
{
	int t;
	cin>>t;
	for(int z=0;z<t;z++)
	{
		int m,n;
		cin>>n>>m;
		int c=fun(n,m);
		if(c==0)
			cout<<"Case #"<<z+1<<": NO";
		else
			cout<<"Case #"<<z+1<<": YES";
		cout<<endl;
	}
	return 0;
}