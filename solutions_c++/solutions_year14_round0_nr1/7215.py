#include <stdio.h>
#include <iostream>
using namespace std;
int a[4][4], b[4][4];
int main()
{
	int ite, n, m, cnt, val;
	scanf("%d",&ite);
	for(int it=1;it<=ite;it++)
	{
		cnt = 0; val = 1;
		scanf("%d",&n);n--;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&m);m--;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;j++)
			{
				if(a[n][i] == b[m][j])
				{
					cnt++;
					val = a[n][i];
				}
			}
		}
		cout<<"Case #"<<it<<": ";
		if(cnt == 1)
		{
			cout<<val<<endl;
		}
		if(cnt > 1)
		{
			cout<<"Bad magician!"<<endl;
		}
		if(cnt == 0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
