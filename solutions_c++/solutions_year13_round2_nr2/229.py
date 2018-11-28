#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
typedef __int64 int64;
int n;
int64 x,y;
double ss[1000000+55];
double cal(int64 n,int64 need)
{
	int64 f=need-1;
	double ans=ss[need];
	double m,z;
	m=z=1.0;
	int64 i;
	for(i=1;i<=need-1;i++)
	{
		m*=i;
		z*=i;
	}
	int las=1;
	for(i=need;i<=n-1;i++)
	{
		z*=i;
		z/=las;
		las+=1;
		ans+=ss[i+1]*z/m;
	}
	return ans;
}
int main()
{
	int cas=0,cc=0;
	ss[0]=1;
	for(int i=1;i<=1000000;i++)
	 ss[i]=ss[i-1]/2;
	freopen("I:\\ipb.in","r",stdin);
	freopen("I:\\output.txt","w",stdout);
	cin>>cas;
	while(cas--)
	{
	     scanf("%d%I64d%I64d",&n,&x,&y);
	     bool yes=0;
	     if(x==0&&y==0)
	     yes=1;
		 cout<<"Case #"<<++cc<<": ";
		 int64 need=5;
		 int64 be=0;
		 n--;
		 while(need<=n)
		 {
				be+=2;
				if(be>=y)
				{
					if(be-y==abs(x))
					  yes=1;
				}
				n-=need;
				need+=4;
			}
			if(yes)
			{
			    	puts("1.00000000");
				continue;    	 
			}
		 if(x-y>=-(be+1)&&x+y<=(be+1))
		 {
				puts("0.00000000");
				continue;
			}
			be+=2;
			if(n==0)
		   {
			    	puts("0.00000000");
				continue;    	 
			}
			if(be>=y&&be-y==abs(x))
			{
				if(y==be)
				{
					puts("0.00000000");
					continue;
				}
				int64 u=need/2;
				int64 e=n-u;
				int64 r=y+1;
				if(e>=r)
				{
					puts("1.0000000");
				}
				else if(n<r)
				{
					puts("0.000000");
				}
				else
				{
					double p=cal(n,r);
					printf("%.8f\n",p);
				}
			}
			else
			{
				puts("0.00000000");
			}
	}
	return 0;
}
