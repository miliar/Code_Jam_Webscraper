#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for(int x=0;x<t;x++)
	{
		int n,m;
		cin >> n >> m;
		int a[n][m];
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				cin >> a[i][j];
		bool flag = true;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				bool flag1 = true;
				bool flag2 = true;
				int q = a[i][j];
				for(int k=0;k<n;k++)
					if(a[k][j] > q)
						flag1 = false;
				for(int k=0;k<m;k++)
					if(a[i][k] > q) 
						flag2 = false;	
				if(flag1 == false && flag2 == false)
					flag = false;
			}	
		}	
		if(flag) printf("Case #%d: YES\n",x+1);
		else	printf("Case #%d: NO\n",x+1);
	}
	return 0;	
}
