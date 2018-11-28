#include<iostream>
#include<limits.h>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int arr[100][100];
	int Rmax[100],Cmax[100];
	int count=0;
	while(test--)
	{
		count++;
		int n,m;
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			Rmax[i]=INT_MIN;
			for(int j=0;j<m;j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]>Rmax[i])
					Rmax[i]=arr[i][j];
			}
		}
		for(int j=0;j<m;j++)
		{
			Cmax[j]=INT_MIN;
			for(int i=0;i<n;i++)
			{
				if(arr[i][j]>Cmax[j])
					Cmax[j]=arr[i][j];
			}
		}
		int flag=1;
		char ans[5];
		strcpy(ans,"YES");
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(arr[i][j]==Rmax[i])
				{
					flag=1;
				}
				else if(arr[i][j]==Cmax[j])
				{
					flag=1;
				}
				else
				{
					flag=0;
					strcpy(ans,"NO");
					break;
				}
			}
		}
		printf("Case #%d: %s\n",count,ans);
	}
	return 0;
}


