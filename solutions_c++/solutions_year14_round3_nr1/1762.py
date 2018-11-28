#include "stdio.h"
#include "iostream"

unsigned gcd ( int m,int n )
{
int temp;
if (m<n)
{
temp=m;
m=n;
n=temp;
}
if ( m % n == 0)return n;
else return gcd ( n,m % n) ;
}

int main()
{
	FILE * finp;
	FILE * foutp;

	int t,n,an,ab;
	int a,b,c;

	finp=fopen("A-small-attempt0.in","r");
	foutp=fopen("1.out","w");

	fscanf(finp,"%d",&t);

	for(int i=0;i<t;i++)
	{
		fscanf(finp,"%d/%d",&a,&b);
		c=gcd(a,b);
		a/=c;b/=c;
		ab=1;an=0;
		if(a>b)ab=0;
		int b1=b;
		while(b1)
		{
			if(b1%2!=0&&b1!=1){ab=0;break;}
			b1/=2;
			an++;
			if (b1==1) break;
		}
		for(int i=1;i<an;i++)
		{
			a*=2;
			if(a>=b) an=i;
		}

		
		if(ab)
		fprintf(foutp,"Case #%d: %d\n",i+1,an);
		else fprintf(foutp,"Case #%d: impossible\n",i+1);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}

