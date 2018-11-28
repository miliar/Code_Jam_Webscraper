#include<stdio.h>
#include<conio.h>
int palin(int);
int prft(int);
int frsqr(int);
void main()
{
FILE *ifp, *ofp;
char outfname[]="zzz.out";
ifp=fopen("C-SMAL~1.in","r");
ofp=fopen(outfname,"w");
int cnt,i=0,j,t;
int a,b;
clrscr();
fscanf(ifp,"%d",&t);
while(!feof(ifp))
{	cnt=0;
	fscanf(ifp,"%d",&a);
	fscanf(ifp,"%d",&b);
	for(j=a;j<=b;j++)
	{   if(frsqr(j)==1)
		cnt=cnt+1;
	}
	fprintf(ofp,"Case #%d: %d\n",++i,cnt);
}
fclose(ifp);
fclose(ofp);
getch();
}
int frsqr(int n)
{       int a,b;
	a=prft(n);
	if(palin(n)==1 && a!=0 && palin(a)==1)
		b=1;
	else
		b=0;
	return b;
}
int palin(int n)
{       int r,m,p=0;
	m=n;
	while(n!=0)
	{	r=n%10;
		p=p*10+r;
		n=n/10;
	}
	if(m==p)
		return 1;
	else
		return 0;
}
int prft(int n)
{       int i,j;
	for(i=1;i<=n;i++)
	{	if(i*i==n)
		{	j=i;
			break;
		}
		else if(i*i>n)
		{	j=0;
			break;
		}
	 }
	return j;
}