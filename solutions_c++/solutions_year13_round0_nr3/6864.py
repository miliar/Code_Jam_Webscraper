#include<stdio.h>
#include<conio.h>
#include<math.h>
int count;

int reverse(int m)
{
int i,d=0,n,k,j;
n=m;
while(n!=0)
	{
	j=n%10;
	n=n/10;
	d=d*10+j;
	}
//printf("%d->%d  ",m,d);
if(d==m)
	return 1;
else return 0;
}


int main()
{
int t,a,b,i,k,fa,fb,x;
clrscr();
FILE *fp,*fp1;
//printf("enter test cases\n");
fp=fopen("C-small-attempt3.in","r");
fp1=fopen("2.in","w");
fscanf(fp,"%d",&t);
for(k=0;k<t;k++)
{
//printf("enter a and b\n");
fscanf(fp,"%d %d",&a,&b);
count=0;

for(i=a;i<=b;i++)
	{
	x=sqrt(i);
	fa=0;fb=0;
	if(x*x==i)
		fa=reverse(i);
	if(fa==1)
		fb=reverse(x);
	if(fb==1)
		count++;
	}


fprintf(fp1,"Case #%d: %d\n",k+1,count);
}
getch();
return 0;
}

