#include<stdio.h>

long long powerof2[64];

inline bool isPowerof2(long long &a)
{
	for(int i =1;i<41;i++)
	{
		if(powerof2[i] == a)
		{
			return true;
		}
	}	
	return false;
}

long long gcd(long long a, long long b)
{
        long long r;
        while(b != 0)
        {
                r = a % b;
                a = b;
                b = r;
        }
        return a;
}

int main()
{
	int T;
	long long P,Q;
	char c;
	scanf("%d",&T);
	powerof2[0] = 1;
	for(int i=1;i<64;i++)
	{
		powerof2[i] = powerof2[i-1] + powerof2[i-1];
	}
	for(int i=1;i<=T;i++)
	{
		scanf("%lld%c%lld",&P,&c,&Q);

		long long l = gcd(P,Q);
		if(l>1)
		{
			P /= l;
			Q /= l;
		}
		int parent = 0;
		if(!isPowerof2(Q))
		{
			printf("Case #%d: impossible\n",i);
			continue;
		}
		


		Q = Q >> 1;
		parent++;
		while(Q)
		{
			if(P>=Q)
			{
				break;				
			}
			if(P>1)
			{
				P--;
			//	printf("%lld %lld\n",P,Q);
				while(P%2==0)
				{
					P = P >> 1;
					Q = Q >> 1;
				}
			//	printf("*%lld %lld\n",P,Q);
			}
			Q = Q >> 1;
			parent++;
		}
		printf("Case #%d: %d\n",i,parent);
	}
	return 0;
}
