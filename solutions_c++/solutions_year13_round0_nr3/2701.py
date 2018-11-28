#include <stdio.h>

int n ;
int nl[10];

int isFair(int x) {
	int t = 0;
	int tx = x;
	while (tx) {
		t = 10*t + tx%10;
		tx /= 10;
	}
	return x == t;
}

int main() {

	int T,N,M;
	int rt ;
	scanf("%d\n", &T);
	for (int i = 1 ; i < 100; i++)
	{
		if (isFair(i) && isFair(i*i))
		{
			nl[n++] = i*i;
		}
		if (i*i > 1000)
		{
			break;
		}
	}
	for (int k = 1 ; k <= T ; k++)
	{
		scanf("%d%d", &N, &M);
		rt = 0;
		for (int i = 0; i < n ; i++)
		{
			if (nl[i] >= N && nl[i] <= M)
			{
				rt++;
			}else
			if (nl[i] > M)
			{
				break;
			}
		}

		printf("Case #%d: %d\n", k, rt);
		
	}
}