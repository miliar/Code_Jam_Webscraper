#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
	int n, m, t, a[4][4], b[4][4], ans;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		scanf("%d", &n);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		
		scanf("%d", &m);
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		int c = 0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[n-1][i] == b[m-1][j])
				{
					c++;
					ans = a[n-1][i];
				}
			}
		}
		if(c == 1)
		{
			cout<<"Case #"<<k<<": "<<ans<<endl;
		}
		else if(c>1)
		{
			cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		}
	}


return 0;
}