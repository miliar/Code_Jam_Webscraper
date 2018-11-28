#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<fstream>
#include<string>

using namespace std;


int main()
{
	int no;
	cin >> no;

	for(int i=1;i<=no;i++)
	{

		int n,m;
		cin >> n >> m;


		int a[n][m];
		bool c[n][m];

		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				cin >> a[j][k];
				c[j][k]=0;
			}
		}

		while(1)
		{
			int max=0;
			for(int j=0;j<n;j++)
			{
				for(int k=0;k<m;k++)
				{

					if (a[j][k]>max && c[j][k]==0)
						max=a[j][k];
				}


			}


			int flag;
			for(int j=0;j<n;j++)
			{
				flag=0;
				for(int k=0;k<m;k++)
				{

					if (a[j][k]>max)
						flag=1;
				}
				if (flag==0)
				{
					for(int k=0;k<m;k++)
					{

						if (a[j][k]==max)
							c[j][k]=1;
					}
				}


			}
			for(int j=0;j<m;j++)
			{
				flag=0;
				for(int k=0;k<n;k++)
				{

					if (a[k][j]>max)
						flag=1;
				}
				if (flag==0)
				{
					for(int k=0;k<n;k++)
					{

						if (a[k][j]==max)
							c[k][j]=1;
					}
				}


			}
			flag=0;
			for(int j=0;j<n;j++)
			{
				for(int k=0;k<m;k++)
				{

					if (a[j][k]==max && c[j][k]==0)
						flag=1;
				}


			}
			if (flag==1)
			{
				cout << "Case #" << i << ": NO\n";
				break;
			}
			flag=0;
			for(int j=0;j<n;j++)
			{
				for(int k=0;k<m;k++)
				{

					if (c[j][k]==0)
						flag=1;
				}


			}
			if (flag==0)
			{
				cout << "Case #" << i << ": YES\n";
				break;
			}

		}


	}


	return 0;
}


























