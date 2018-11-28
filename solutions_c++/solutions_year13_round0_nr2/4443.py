#include <stdio.h>
#include <memory.h>
#include <iostream>
#define MAX 104

using namespace std;

int main()
{	
	int t;
	cin >> t;
	for(int T=1;T<=t;T++)
	{
		int n,m;
		int arr[MAX][MAX];
		memset(arr,0,sizeof(arr));
		cin >> n >> m;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				cin >> arr[i][j];
		int flag=true;
		for(int i=0;i<n&&flag;i++)
		{
			for(int j=0;j<m&&flag;j++)
			{
				int c1,c2;
				c1=c2=0;
				for(int k=0;k<n;k++)
					c1+=arr[k][j]>arr[i][j];
				for(int k=0;k<m;k++)
					c2+=arr[i][k]>arr[i][j];
				if( c1 && c2 ) flag=false;
			}
		}
		if( flag )
			printf("Case #%d: %s\n",T,"YES");
		else
			printf("Case #%d: %s\n",T,"NO");
	}
	return 0;
}