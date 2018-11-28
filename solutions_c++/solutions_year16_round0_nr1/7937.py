#include<cstdio>
using namespace std;

int val[10];

int check()
{
	int i,x;
	for(i=0;i<10;i++)
	{
		if(val[i]!=i)
			return 0;
	}
	return 1;
}

int rem(int n)
{
	int x,i;
	
	while(n>=10)
	{
		x=n%10;
		val[x] = x;
		n = n/10;
	
	}
	val[n]=n;
}

int main()
{
	int n,i,m,t;
	
	scanf("%d", &t);
	while(t--)
	{
		
   int chk=0,mul=1,cases=0;	
   
	for(i=0;i<10;i++)
	{
		val[i]=-1;
	}
	scanf("%d",&n);
	if(n==0)
	{
		printf("Case #%d: Insomnia\n", ++cases);
	}
	else
	{
	while(chk==0)
	{
		m=n;
		m=mul*n;
		rem(m);
	
		chk = check();
		mul = mul+1;
		

	}
	
	chk=0;
	mul=1;
	
	printf("Case #%d:  %d\n", ++cases, m );

}	
}

return 0;
}

