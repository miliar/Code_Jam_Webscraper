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
 	 int t,x1;
 	 inp(t);
 	 for(x1=1;x1<=t;x1++)
 	 {
 	 	double c,x,f,time=0,p,p1,p2;
 	 	int farm=0,rate=0,rate1=0;
 	 	scanf("%lf %lf %lf",&c,&f,&x);
 	 	while(1)
 	 	{
 	 		rate=(farm*f)+2;
 	 		rate1=((farm+1)*f)+2;
 	 		p=(x/rate);
 	 		p1=(c/rate);
 	 		p2=(x/rate1);
 	 		//printf("p=%.7lf nex=%.7lf time=%.7lf\n",p,(p1+p2),time);
 	 		if(p<=(p1+p2))
 	 		{
 	 			time+=p;
 	 			break;
 	 		}
 	 		farm++;
 	 		time+=p1;
 	 	}
 	 	printf("Case #%d: %.7lf\n",x1,time);
 	 }
 	 return 0;
}
