#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;
struct power{
	int num ;
	int powe;
};
power a[10005];
int counter=0;
int checksqr(char p[])
{
	char c[1000];
	strcpy(c,p);
	int l=strlen(p);
	int i;
	l=l-1;
	for(i=0;i<l;i++)
	{
		if(c[l-i]!=p[i])
			return 0;
	}
	return 1;
}
int checknum(char n[])
{
	char c[1000];
	strcpy(c,n);
	int l=strlen(n);
	l=l-1;
	int i;
	for(i=0;i<l;i++)
	{
		if(c[l-i]!=n[i])
			return 0;
	}
	return 1;
}
void change(int x )
{
	int s;
	s=sqrt(x);
	if(s*s==x){
	char p[1000];
	char n[1000];
	int i , j;
	p[0]=0;
	i=0;
	while(x>0)
	{
		p[i]=x%10+'0';
		x/=10;
		i++;
	}
	p[i]=0;
 	j=0;
 	n[0]=0;
 	while(s>0)
 	{
 		n[j]=s%10+'0';
 		s/=10;
 		j++;
 	}
 	n[j]=0;
 	int t1=checknum(n);
 	int t2=checksqr(p);
 	if(t1==1&&t2==1)
 		counter++;
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	memset(a,0,10005);
	for(int i=0;i*i<=1000;i++)
	{
		a[i].num=i;
		a[i].powe=i*i;
	}
	int c=1;
	int t;
	cin >> t;
	while(t--)
	{
		int x , y;
		cin >> x >> y;
		int i ;
		for(i=min(x,y);i<=max(x,y);i++)
		{
			change(i);
		}
		printf("Case #%d: %d\n",c,counter);
		c++;
		counter=0;
	}
	return 0;
}
