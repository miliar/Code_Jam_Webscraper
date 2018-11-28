#include<cstdio>

int main()
{
	int n;scanf("%d", &n);
	int A, B, K, citac=0;
	for(int i=0;i<n;++i)
	{
	scanf("%d %d %d", &A, &B, &K);
	for(int a=0;a<A;++a)for(int b=0;b<B;++b)if( (a&b) < K)citac++;
	printf("Case #%d: %d\n", i+1, citac);
	citac=0;
	}
	return 0;
}