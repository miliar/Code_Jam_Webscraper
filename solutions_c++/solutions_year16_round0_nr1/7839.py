#include <cstdio>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		int N;
		scanf("%d", &N);
		int bit = 0;
		if(N==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		int i = 0;
		while(bit != (1 << 10) - 1)
		{
			++i;
			long long x = (long long)N * i;
			while(x != 0)
			{
				bit |= (1 << (x % 10));
				x /= 10;
			}
		}
		printf("%lld\n", (long long)N * i);
	}
}