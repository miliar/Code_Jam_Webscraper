#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int iter=0;iter<T;iter++)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		int arr[n][m],max=-1,maxi=-1,maxj=-1,mat[n][m],flag=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d",&arr[i][j]);
				if(arr[i][j]>max)
				{
					max=arr[i][j];
					maxi=i;
					maxj=j;
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				mat[i][j]=max;
			}
		}
		for(int i=0;i<m;i++)
		{
			if(mat[maxi][i]!=arr[maxi][i])
			{
				for(int j=0;j<n;j++)
					mat[j][i]=arr[maxi][i];
			}
		}
		for(int i=0;i<n;i++)
		{
			if(mat[i][maxj]!=arr[i][maxj])
			{
				for(int j=0;j<m;j++)
				{
					mat[i][j]=min(mat[i][j],arr[i][maxj]);
				}
			}			
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
//				cout<<mat[i][j]<<" ";
				if(arr[i][j]!=mat[i][j])
				{
					flag=1;
					break;
				}
			}
//			cout<<"\n";
			if(flag==1)
				break;
		}
		if(flag==0)
			printf("Case #%d: YES\n",iter+1);
		else
			printf("Case #%d: NO\n",iter+1);
	}
}
