#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;

const int maxn=110,INF=1000000000;
int a[maxn][maxn];
bool f[maxn][maxn],row[maxn],column[maxn];
int cnt,m,n,minn,maxx,x,t;
bool flag,judge;

void close()
{
exit(0);
}

void work()
{
	memset(f,false,sizeof(f));
	memset(row,false,sizeof(row));
	memset(column,false,sizeof(column));
	cnt=n+m;
	while (cnt!=0)
	{
		judge=false;
		for (int i=1;i<=n;i++) //ȡ�����������������С�ڵ�������δȡ��������С��
		{
			if (row[i]) continue;
			flag=false;
			minn=INF;maxx=0;
			for (int j=1;j<=m;j++) //�ظ�
				if (not f[i][j])
				{
					x=a[i][j];
					break;
				}
			for (int j=1;j<=m;j++)
				if (not f[i][j] && x!=a[i][j])
				{
					flag=true;
					break;
				}
			if (flag) continue;
			for (int j=1;j<=m;j++)
			{
				if (f[i][j] && a[i][j]>maxx) //ȡ��
					maxx=a[i][j];
				if (not f[i][j] && minn>a[i][j])
					minn=a[i][j];
				if (maxx>minn)
				{
					flag=true;
					break;
				}
			}
			if (not flag)
			{
				row[i]=true;
				judge=true;
				for (int j=1;j<=m;j++)
					f[i][j]=true; //��һ�ж��ϸ���
				cnt--;
			}
		}
		for (int j=1;j<=m;j++) //ȡ�����������������С�ڵ�������δȡ��������С��
		{
			if (column[j]) continue;
			flag=false;
			minn=INF;maxx=0;
			for (int i=1;i<=n;i++) //�ظ�
				if (not f[i][j])
				{
					x=a[i][j];
					break;
				}
			for (int i=1;i<=n;i++)
				if (not f[i][j] && x!=a[i][j])
				{
					flag=true;
					break;
				}
			if (flag)continue;
			for (int i=1;i<=n;i++)
			{
				if (f[i][j] && a[i][j]>maxx) //ȡ��
					maxx=a[i][j];
				if (not f[i][j] && minn>a[i][j])
					minn=a[i][j];
				if (maxx>minn)
				{
					flag=true;
					break;
				}
			}
			if (not flag)
			{
				column[j]=true;
				judge=true;
				for (int i=1;i<=n;i++)
					f[i][j]=true; //��һ�ж��ϸ���
				cnt--;
			}
		}
		if (not judge)
		{
			printf("NO\n");
			return;
		}
	}
	printf("YES\n");

}

void init()
{
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		scanf("%d %d",&n,&m);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				scanf("%d",&a[i][j]);
		work();
	}
}

int main ()
{
	init();
	close();
	return 0;
}

