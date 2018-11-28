#include <stdio.h>
struct str{
	int x0;
	int y0;
}y[10010];
int s=1;
void solve(int);
int main()
{
	//freopen("Asmall.in","r",stdin);
	freopen("Alarge.in","r",stdin);
	freopen("output.txt","w",stdout);
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++) solve(i);
}
int a,b,count;
int direx[10]={1,0,-1,0};
int direy[10]={0,1,0,-1};
int check[10010],control;
char x[110][110];
int z[110][110];
void clear()
{
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			z[i][j]=0;
		}
	}
	for(int i=0;i<=10001;i++) check[i]=0;
}
void func(int k)
{
	int c,d,e;
	check[k]=1;
	c = y[k].x0;
	d = y[k].y0;
	if(x[c][d]=='v') e=0;
	if(x[c][d]=='>') e=1;
	if(x[c][d]=='^') e=2;
	if(x[c][d]=='<') e=3;
	int x1=c,y1=d;
	while(1)
	{
		x1+=direx[e];
		y1+=direy[e];
		if(1<=x1&&x1<=a);
		else break;
		if(1<=y1&&y1<=b);
		else break;
		if(x[x1][y1]!='.')
		{
			if(check[z[x1][y1]]==0)
			{
				func(z[x1][y1]);
			}
			return;
		}
	}
	for(int i=0;i<4;i++)
	{
		x1=c;
		y1=d;
		while(1)
		{
			x1+=direx[i];
			y1+=direy[i];
			if(1<=x1&&x1<=a);
			else break;
			if(1<=y1&&y1<=b);
			else break;
			if(x[x1][y1]!='.')
			{
				count++;
				return;
			}
		}
	}
	control=1;
}
void solve(int T)
{
	int i,j;
	s=1;
	control=0;
	count=0;
	clear();
	scanf("%d%d",&a,&b);
	for(i=1;i<=a;i++) scanf("%s",x[i]+1);
	for(i=1;i<=a;i++)
	{
		for(j=1;j<=b;j++)
		{
			if(x[i][j]!='.')
			{
				y[s]={i,j};
				z[i][j]=s;
				s++;
			}
		}
	}
	for(i=1;i<s;i++)
	{
		if(check[i]==0)
		{
			func(i);
			if(control)
			{
				printf("Case #%d: IMPOSSIBLE\n",T);
				return;
			}
		}
	}
	printf("Case #%d: %d\n",T,count);
}
