#include <bits/stdc++.h>
using namespace std;

int getmask(long long n)
{
	int mask = 0;
	while(n){
		mask |= 1 << (n % 10);
		n /= 10;
	}
	return mask;
}
int test(int n)
{
	int mask = 0;
	int full = (1 << 10) - 1;
	for(int i = 1 ; i <= 100 ; i++)
	{
		mask |= getmask((long long)(i) * n);
		if(mask == full)return i;
	}
	return -1;
}

int main()
{
	int T;
	scanf("%d" , &T);
	for(int tt = 1 ; tt <= T ; tt++)
	{
		printf("Case #%d: " , tt);
		int n;scanf("%d"  ,&n);
		if(n == 0)printf("INSOMNIA\n");
		else
			printf("%lld\n" , n * test(n));
	}
	return 0;
}