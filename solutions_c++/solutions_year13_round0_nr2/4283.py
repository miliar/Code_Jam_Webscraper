#include <stdio.h>

using namespace std;

int n,m,a[120][120];

bool CheckVertical(int x,int f)
{
	//int f = 1;//a[0][x];
	for(int i = 0;i < n;i++)
	if(a[i][x] != f && a[i][x] != -1)return false;
	return true;
}

void MarkVertical(int x)
{
	for(int i = 0;i < n;i++)
	a[i][x] = -1;
	return;
}

bool CheckHorizontal(int x,int f)
{
	//int f = 1;//a[x][0];
	for(int i = 0;i < m;i++)
	if(a[x][i] != f && a[x][i] != -1)return false;
	return true;
}

void MarkHorizontal(int x)
{
	for(int i = 0;i < m;i++)
	a[x][i] = -1;
	return;
}

int main()
{
	freopen("bsmall.in","r",stdin);
	freopen("bsmall.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int q = 0;q < t;q++)
	{
		scanf("%d%d",&n,&m);
		for(int i = 0;i < n;i++)
		for(int j = 0;j < m;j++)
		scanf("%d",&a[i][j]);
		
		for(int p = 1;p < 101;p++)
		{
			for(int i = 0;i < m;i++)
			if(CheckVertical(i,p))MarkVertical(i);
			for(int i = 0;i < n;i++)
			if(CheckHorizontal(i,p))MarkHorizontal(i);
		}
		
		bool f = false;
		for(int i = 0;i < n;i++)
		{
			for(int j = 0;j < m;j++)
			//if(a[i][j] == 1)
			if(a[i][j] != -1)
			{
				f = true;
				break;
			}
			if(f)break;
		}
		
		if(f)printf("Case #%d: NO\n",q+1);
		else printf("Case #%d: YES\n",q+1);
	}
	return 0;
}
