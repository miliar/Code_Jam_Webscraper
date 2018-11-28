#include <cstdio>

typedef unsigned u32;
int main()
{
	u32 N=16,J=50;
	puts("Case #1:");
	int cnt=0;
	for(register u32 K=(1<<(N-1))+1;K<(1<<N);K+=2)
	{
		bool ss=1;
		long long key[11];
		for(int b=2;b<=10;b++)
		{
			long long M=0,p;
			for(int i=15;i>=0;i--) M=M*b+((K>>i)&1);
			bool s=false;
			for(p=2;p*p<=M;p++)
				if(M%p==0){
					s=1;break;
				}
			if(!s) 
			{
				ss=0;
				break;
			}else key[b]=p;
		}
		if(!ss) continue;
		for(int i=15;i>=0;i--) printf("%d",(K>>i)&1);
		for(int b=2;b<=10;b++) printf(" %I64d", key[b]);
		puts("");
		if(++cnt==J)break;
	}
	return 0;
}
