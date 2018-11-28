#include <stdio.h>
#include <math.h>

int d_f(long long int num)
{
double a,b,c;
a=log10(num); b=(int)a;

int ans;
if(a==b) ans=a+1;
else { a=ceil(a); ans=a; }

return ans;
}

long long int ch(int dig[])
{
int i,yep=1;
for(i=0;i<=9;i++)
	{
	if(dig[i]==0) { yep=0; break; }
	}

return yep;
}

void di(long long int num,int dig[])
{
int i;
long long int digit,mod,div,d;
digit=d_f(num);

for(i=1;i<=digit;i++)
	{
	mod=pow(10,i); div=pow(10,i-1);
	d=(num % mod)/div;
	dig[d]++;
	}
}

int main()
{
int p,q; scanf("%d",&p);

int dig[10];
for(q=0;q<p;q++)
{
long long int k=0,i,n,num;
for(i=0;i<=9;i++) dig[i]=0;
scanf("%lld",&n);

if(n==0) { printf("Case #%d: INSOMNIA\n",q+1); continue; }


for(i=1;;i++)	{

num=n*i;
di(num,dig);
k=ch(dig);

if(k==1)
	{
	printf("Case #%d: %lld\n",q+1,num);
	break;
	}
else continue;
}

}

return 0;
}
