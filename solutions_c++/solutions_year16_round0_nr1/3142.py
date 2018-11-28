#include <stdio.h>
#include <string.h>

int T, N, ans;

int cnt;
int arr[20];

void check(long long n)
{
	long long r;
	
	do
	{
		r = n % 10;
		n = (n - r)/10;
		if(arr[r] == 0)
		{
			arr[r] = 1;
			cnt--;
		}
	}while(n != 0);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for(int cs = 1; cs <= T; cs++)
	{
		scanf("%d", &N);

		if(N == 0)
		{
			printf("Case #%d: INSOMNIA\n", cs);
			continue;
		}

		memset(arr, 0, sizeof(int) * 20);
		long long ans = 0;
		cnt = 10;
		while(cnt != 0)
		{
			ans += N;
			check(ans);
		}
		

		printf("Case #%d: %d \n", cs, ans);
	}

}