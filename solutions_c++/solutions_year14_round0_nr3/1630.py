#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int res[60][60];
int n,m,num;

bool Ok(int r,int c,int cnt)
{
	if (r==1 && c==1) return true;
	if (r==1 || c==1) return false;
	if (min(r,c)==2) return cnt==0;
	return cnt<=(r-2)*(c-2);
}

bool empty(int x,int y)
{
	if (x<1 || x>n || y<1 || y>m) return true;
	return res[x][y];
}

int main()
{
	freopen("input2.in","r",stdin);
	freopen("output2.out","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	
	for (int ii=1;ii<=Test;++ii)
	{
		scanf("%d%d%d",&n,&m,&num);
		int space=n*m-num;
		memset(res,0,sizeof(res));
		bool find=false;
		printf("Case #%d:\n",ii);
		if (n==1 || m==1)
		{
			for (int i=1;i<=n;++i)
				for (int j=1;j<=m;++j)
					res[i][j]=1;
			for (int i=1;i<=num;++i)
				if (n==1) res[1][i]=0;
					else res[i][1]=0;
			res[n][m]=2;
			find=true;
		}
		else
		{
			for (int i=1;i<=n && !find;++i)
				for (int j=1;j<=m;++j)
					if (i*j>=space && i*j-space<n && i*j-space<m)
					{
						int rest=i*j-space;
						if (Ok(i,j,i*j-space))
						{
							for (int r=1;r<=i;++r)
								for (int c=1;c<=j;++c)
									res[r][c]=1;
							for (int i1=i;i1>=3 && rest>0;--i1)
								for (int j1=j;j1>=3 && rest>0;--j1)
								{
									res[i1][j1]=0;
									--rest;
								}
							res[1][1]=2;
							find=true;
							break;
						}
					}
		}
		if (!find) printf("Impossible\n");
		else
			for (int i=1;i<=n;++i)
			{
				for (int j=1;j<=m;++j)
				{
					if (res[i][j]==1) printf(".");
					if (res[i][j]==0) printf("*");
					if (res[i][j]==2) printf("c");
				}
				printf("\n");
			}
	}
	
	return 0;
}
	