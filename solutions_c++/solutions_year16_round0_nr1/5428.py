#include <bits/stdc++.h>

int c1,c2,c3,c4,c5,c6,c7,c8,c9,c0;

void frequencia (int n)
{
	while (n>0)
	{
		if (n%10==0) c0++;
		if (n%10==1) c1++;
		if (n%10==2) c2++;
		if (n%10==3) c3++;
		if (n%10==4) c4++;
		if (n%10==5) c5++;
		if (n%10==6) c6++;
		if (n%10==7) c7++;
		if (n%10==8) c8++;
		if (n%10==9) c9++;
		n /= 10;
	}
}



int main (void)
{
	int T,t=1;
	scanf("%d",&T);
	while(t<=T)
	{
		c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c0=0;
		int a,n,b,i=1;
		scanf("%d",&n);
		a=n;
		if(n==0) printf("Case #%d: INSOMNIA\n",t);
		else
		{
			while (c1 == 0 or c2==0 or c3 == 0 or c4 == 0 or c5 == 0 or c6 == 0 or c7 == 0 or c8 == 0 or c9 ==0 or  c0 == 0)
			{
				frequencia(a);
				i++;
				a=n*i;
				b=n*i;
			}
			printf("Case #%d: %d\n",t,b*(i-1)/i);
		}
		t++;
	}
}