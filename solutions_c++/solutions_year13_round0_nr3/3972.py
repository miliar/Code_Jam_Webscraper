/*#include<stdio.h>
char a[4][4];
bool draw;
void input()
{
	int i, j, k=0;
	for(i=0; i<4; i++)
		scanf("%s",a[i]);
	for(i=0;i<4; i++)
		for(j=0;j<4;j++)	
		{
			if(a[i][j]=='X')
				a[i][j]=1;
			else if(a[i][j]=='O')
				a[i][j] = 2;
			else if(a[i][j] == 'T')
				a[i][j] = 3;
			else{
				a[i][j] = 0;
				k++;
			}
		}
	if(k)
		draw = false;
	else
		draw = true;
}
void process()
{
	int i, j, k, l,o,p,q;
	k = l = 0;

	for(i=0; i<4; i++)
		for(j=0; j<4; j++)
		{
			p=q=0;
			for(o=0; i+o<4; o++)
			{
				if(a[o+i][j]&1)
					p++;
				if(a[o+i][j]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
			p=q=0;
			for(o=0; j+o<4; o++)
			{
				if(a[i][j+o]&1)
					p++;
				if(a[i][j+o]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
			p=q=0;
			for(o=0; j+o<4 && i-o>=0; o++)
			{
				if(a[i-o][j+o]&1)
					p++;
				if(a[i-o][j+o]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
			
			p=q=0;
			for(o=0; j+o<4 && i+o<4; o++)
			{
				if(a[i+o][j+o]&1)
					p++;
				if(a[i+o][j+o]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
		}
	if(k & l)
		printf("Draw");
	else if(k)
		printf("X won");
	else if(l)
		printf("O won");
	else
	{
		if(draw)printf("Draw");
		else printf("Game has not completed");
	}
	printf("\n");
}
void output()
{
}
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);

	int t,v;
	scanf("%d",&t);
	for(v=1; v<=t; v++)
	{
		printf("Case #%d: ",v);
		input();
		process();
		output();
	}
}*/

#include <stdio.h>
#include <math.h>
long long int a,b;
long long int d[40];
int dl;
void input()
{
	scanf("%lld %lld",&a,&b);
}
int palim(long long int j)
{
	int a[100];
	int i;
	for(i=0; j; i++)
	{
		a[i]=j%10;
		j/=10;
	}
	for(j=0; j<i/2; j++)
		if(a[j] != a[i-j-1])
			return 0;
	return 1;
}
void process()
{
	int i, j;
	for(i=0;i<dl;i++)
	{
		if(d[i]>=a)break;
	}
	j=i;
	for(;i<dl;i++)
		if(d[i]>b)break;
	printf("%d\n",i-j);
}
void output()
{
}
void inil()
{
	long long int i, j, l=1;
	for(i=l*l; i<=100000000000000; i+=(2*l+1),l++)
	{
		if(palim(l) && palim(l*l))
		{
			d[dl++] = i;
		}
	}
}
int main()
{
	freopen("C-large-1.in","rt",stdin);
	freopen("output.txt","wt",stdout);

	int t,v;
	scanf("%d",&t);
	inil();
	for(v=1; v<=t; v++)
	{
		printf("Case #%d: ",v);
		input();
		process();
		output();
	}
}