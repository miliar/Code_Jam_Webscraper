#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;

int gcd(int p, int q);

int main()
{
	int T;
	int a,b,D,t=0;
	double temp;
	FILE *fp1,*fp2;

	fp1=fopen("A-small-attempt8.in","r");
	fp2=fopen("A-small-attempt8.out","w+");

	fscanf(fp1,"%d",&T);

	for(int i=0;i<T;i++)
	{
		fscanf(fp1,"%d/%d",&a,&b);
		t=0;
		D=gcd(b,a);

		a/=D;
		b/=D;

		temp=log((double)b)/log(2.0);
		while(b!=0)
		{
			if(b<=a)
				break;
			b/=2;
			t++;
		}
		if((int)temp==temp)
			fprintf(fp2,"Case #%d: %d\n",i+1,t);
		else
			fprintf(fp2,"Case #%d: impossible\n",i+1);
	}

	return 0;
}

int gcd(int p, int q)
{
	if (q == 0) return p;
	return gcd(q, p%q);
}