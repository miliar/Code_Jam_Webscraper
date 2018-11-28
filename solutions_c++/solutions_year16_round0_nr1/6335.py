#include<stdio.h>
long long solve(int n)
{
	long long x = 0, t;
	int bf = 0;
	for(;bf<(1<<10)-1;)
	{
		t = (x+=n);
		do{
			bf |= ( 1<<(t%10) );
		}while((t/=10)!=0);
	}
	return x;
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int TT=1; TT<=T; TT++)
	{
		int n;
		scanf("%d", &n);
		if(n==0) printf("Case #%d: INSOMNIA\n", TT);
		else printf("Case #%d: %lld\n", TT, solve(n)); 
	}
	return 0;
}
