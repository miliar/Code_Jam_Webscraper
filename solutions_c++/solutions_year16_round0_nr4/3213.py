#include <cstdio>
#include <iostream>
unsigned long long ppow(int K, int C, int input)
{
	unsigned long long num = input;
	for(int i=1; i< C; i++)
	{
		num =(unsigned long long)num*K+input;
	}
	return num+1;
}
int main(void)
{
	int T;
	std::cin >> T;
	for (int t=1; t <= T; t++)
	{
		int K,C,S;
		scanf("%d",&K); scanf("%d",&C); scanf("%d",&S);
		printf("Case #%d: ",t);
		for(int i=0; i<S; i++)
		{
			unsigned long long point = ppow(K,C,i);
			printf("%lld ",point);
		}
		printf("\n");
	}
}
