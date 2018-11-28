#include <cstdio>

int digits_inside(int N)
{
	int ret = 0;
	while(N)
	{
		int d = N % 10;
		ret |= 1 << d;
		N /= 10;
	}
	return ret;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int caseno = 1; caseno <= T; caseno++)
	{
		int N;
		scanf("%d", &N);
		if(N == 0){
			printf("Case #%d: INSOMNIA\n", caseno);
			continue;
		}
		int temp = N;
		int digits_found = digits_inside(temp);
		while(digits_found != 1023)
		{
			temp += N;
			digits_found |= digits_inside(temp);
		}
		printf("Case #%d: %d\n", caseno, temp);
	}
	return 0;	
}
