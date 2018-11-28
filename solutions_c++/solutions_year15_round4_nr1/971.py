#include <stdio.h>
#include <string.h>

#define TEST_NUM 2

char inname[100];
char outname[100];

char arr[110][110];

bool chk[110][110];
bool vit[110][110];

int dx[4]={1, 0, -1, 0};
int dy[4]={0, 1, 0, -1};

void process()
{
	memset(chk, 0, sizeof(chk));
	memset(vit, 0, sizeof(vit));
	int r, c, cnt=0, x, y, t, i, j, k;
	scanf("%d%d", &r, &c);
	for(i=0;i<r;i++)
		scanf("%s", arr[i]);
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			if(arr[i][j]!='.')
			{
				for(k=0;k<4;k++)
				{
					x=i;
					y=j;
					while(1)
					{
						x+=dx[k];
						y+=dy[k];
						if(!(0<=x&&x<r&&0<=y&&y<c))
							break;
						vit[x][y]=1;
					}
				}
			}
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			if(arr[i][j]!='.')
			{
				if(arr[i][j]=='<')
				{
					chk[i][j]=1;
					cnt++;
				}
				break;
			}
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=c-1;j>=0;j--)
		{
			if(arr[i][j]!='.')
			{
				if(arr[i][j]=='>')
				{
					chk[i][j]=1;
					cnt++;
				}
				break;
			}
		}
	}
	for(j=0;j<c;j++)
	{
		for(i=0;i<r;i++)
		{
			if(arr[i][j]!='.')
			{
				if(arr[i][j]=='^')
				{
					chk[i][j]=1;
					cnt++;
				}
				break;
			}
		}
	}
	for(j=0;j<c;j++)
	{
		for(i=r-1;i>=0;i--)
		{
			if(arr[i][j]!='.')
			{
				if(arr[i][j]=='v')
				{
					chk[i][j]=1;
					cnt++;
				}
				break;
			}
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			if(chk[i][j]&&!vit[i][j])
			{
				printf("IMPOSSIBLE");
				return;
			}
		}
	}
	printf("%d", cnt);
}

void pre_process()
{

}

int main()
{
	sprintf(inname, "%d.in", TEST_NUM);
	sprintf(outname, "%d.out", TEST_NUM);
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti=1;ti<=tn;ti++)
	{
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}