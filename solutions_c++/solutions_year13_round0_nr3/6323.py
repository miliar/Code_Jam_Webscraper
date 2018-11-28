#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int main()
{
	int i,j,k,arr[100][100],m,n,t,te;
	cin>>t;
	for(te=0;te<t;te++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&arr[i][j]);
			}
		}
		printf("Case #%d: ",te+1);
		if(n==1||m==1)
		{
			printf("YES\n");
			continue;
		}
		j=m;
		for(i=0;i<n&&j==m;i++)
		{
			for(j=0;j<m;j++)
			{
				if(arr[max(0,i-1)][j]<=arr[i][j]&&arr[min(n-1,i+1)][j]<=arr[i][j])
					continue;
				if(arr[i][max(0,j-1)]<=arr[i][j]&&arr[i][min(n-1,j+1)]<=arr[i][j])
					continue;
				break;
			}
		}
		if(i==n)
			printf("YES\n");
		else
			printf("NO\n");
	}
}
