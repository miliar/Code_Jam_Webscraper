#include <cstdio>
#include <memory.h>
using namespace std;
int max(int a,int b)
{
	return a>b?a:b;
}
int main()
{
	int T,n,m;
	int h[100][100];
	bool f1[100][100];
	bool f2[100][100];
	int max1[100][100][2];
	int max2[100][100][2];
	freopen("B-large.in","r",stdin);
	freopen("outlarge","w",stdout);
	scanf("%d",&T);
	for (int c=1;c<=T;++c)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i)
		{
			for (int j=0;j<m;++j)
			{
				scanf("%d",&h[i][j]);
			}
		}

		for (int i=0;i<n;++i)
		{
			max1[i][0][0]=h[i][0];
			for (int j=1;j<m;++j)
			{
				max1[i][j][0]=max(max1[i][j-1][0],h[i][j]);
			}
			max1[i][m-1][1]=h[i][m-1];
			for (int j=m-2;j>=0;--j)
			{
				max1[i][j][1]=max(max1[i][j+1][1],h[i][j]);
			}
		}
		for (int j=0;j<m;++j)
		{
			max2[0][j][0]=h[0][j];
			for (int i=1;i<n;++i)
			{
				max2[i][j][0]=max(max2[i-1][j][0],h[i][j]);
			}
			max2[n-1][j][1]=h[n-1][j];
			for (int i=n-2;i>=0;--i)
			{
				max2[i][j][1]=max(max2[i+1][j][1],h[i][j]);
			}
		}

		bool flag=false;
		for (int i=0;i<n;++i)
		{
			for (int j=0;j<m;++j)
			{
				if((j>0&&max1[i][j-1][0]>h[i][j])||(j<m-1&&max1[i][j+1][1]>h[i][j]))
				{
					f1[i][j]=true;
				}
				else
				{
					f1[i][j]=false;
				}

				if((i>0&&max2[i-1][j][0]>h[i][j])||(i<n-1&&max2[i+1][j][1]>h[i][j]))
				{
					f2[i][j]=true;
				}
				else
				{
					f2[i][j]=false;
				}

				if(f1[i][j]&&f2[i][j])
				{
					flag=true;
					i=n;
					break;
				}
			}
		}
		if(flag)
		{
			printf("Case #%d: NO\n",c);
		}
		else
		{
			printf("Case #%d: YES\n",c);
		}
	}
}