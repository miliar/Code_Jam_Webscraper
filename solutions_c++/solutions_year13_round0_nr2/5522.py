#include<stdlib.h>
#include<stdio.h>

const int LEN = 10;

int arr[LEN][LEN];
int n,m;
bool judgeX(int x,int y);
bool judgeY(int x,int y);
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	
	int T;
	scanf("%d\n",&T);
	for(int t=0;t<T;t++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d",&arr[i][j]);
			}
			
		}
		
		bool res = true;
		for(int i=0;i<n;i++)
		{
			if(res == false)
				break;
			for(int j=0;j<m;j++)//n?m?
			{
				if(arr[i][j]==1)
				{
					bool jx = judgeX(i,j);
					bool jy = judgeY(i,j);

					if(!jx && !jy)
					{
						res = false;
						break;
					}

				}//end of if
			}
		}
		if(res)
		{
			printf("Case #%d: %s\n",t+1,"YES");
		}
		else
		{
			printf("Case #%d: %s\n",t+1,"NO");
		}

	}
	return 0;
}

bool judgeX(int x,int y)
{
	bool ret = true;
	for(int i=0;i<m;i++)
	{
		if(arr[x][i]==2)
		{
			ret = false;
			break;
		}
	}

	return ret;
}
		
bool judgeY(int x,int y)
{
	bool ret = true;
	for(int i=0;i<n;i++)
	{
		if(arr[i][y]==2)
		{
			ret = false;
			break;
		}
	}

	return ret;
}