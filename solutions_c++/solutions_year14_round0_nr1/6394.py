#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#define getcx getchar_unlocked
using namespace std;
inline void inp(int &n) // Fast Input
{
	n=0;
	int ch=getcx();int sign=1;
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
	while( ch >= '0' && ch <= '9' )
	n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
	n=n*sign;
}
void output(int x)  // Fast Output
{
	if(x<0)
	{
		putchar('-');
		x=-x;
	}
    int len=0,data[10];
	while(x)
	{
		data[len++]=x%10;
		x/=10;
	}
	if(!len)
		data[len++]=0;
	while(len--)
		putchar(data[len]+48);
	putchar('\n');
}
int main()
{
 	int a[5][5],b[5][5];
 	int t,x;
 	inp(t);
 	for(x=1;x<=t;x++)
 	{
 		int n,m,i,j,f=0,ans=0;
 		inp(n);
 		for(i=1;i<5;i++)
 		{
 			for(j=1;j<5;j++)
 			inp(a[i][j]);
 		}
 		inp(m);
 		for(i=1;i<5;i++)
 		{
 			for(j=1;j<5;j++)
 			inp(b[i][j]);
 		}
 		for(i=1;i<5;i++)
 		{
 			for(j=1;j<5;j++)
 			{
 			    
 				if(a[n][i]==b[m][j])
 				{
 					f++;
 					ans=b[m][j];
 				}
 			}
 		}
 		if(f==1)
 		printf("Case #%d: %d\n",x,ans);
 		if(f==0)
 		printf("Case #%d: Volunteer cheated!\n",x);
 		if(f>1)
 		printf("Case #%d: Bad magician!\n",x);
 	}
 	return 0;
 }
