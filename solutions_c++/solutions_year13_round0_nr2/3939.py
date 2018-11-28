#include <iostream>

using namespace std;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Problem B. Lawnmower

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int cases,n,m,r[110][110],t[110][110],maxi;
	bool possible;
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>n>>m;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				cin>>r[i][j];
			}
		}
		for(int i=1;i<=n;i++)
		{
			maxi=-1;
			for(int j=1;j<=m;j++)
			{
				if(r[i][j]>maxi)
				{
					maxi=r[i][j];
				}
			}
			for(int j=1;j<=m;j++)
			{
				t[i][j]=maxi;
			}
		}
		for(int j=1;j<=m;j++)
		{
			maxi=-1;
			for(int i=1;i<=n;i++)
			{
				if(r[i][j]>maxi)
				{
					maxi=r[i][j];
				}
			}
			for(int i=1;i<=n;i++)
			{
				if(t[i][j]>maxi)
				{
					t[i][j]=maxi;
				}
			}
		}
		possible=true;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				if(r[i][j]!=t[i][j])
				{
					possible=false;
					break;
				}
			}
			if(!possible)break;
		}
		cout<<"Case #"<<kase<<": ";
		if(possible)
			cout<<"YES\n";
		else
			cout<<"NO\n";
	}
	return 0;
}