#include <cstdio>
#include <algorithm>

using namespace std;

int data[10000];
int n, x;

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int kase = 1; kase <= T; kase++)
	{
		scanf("%d %d", &n, &x);
		for(int i = 0; i < n; i++) scanf("%d", data + i);
		sort(data, data + n);

		int ans = 0;
		for(int i = n - 1; i >= 0; i--)
		{
			if(data[i] == -1) continue;

			for(int j = i - 1; j >= 0; j--)
			{
				if(data[j] == -1) continue;
				if(data[j] + data[i] <= x)
				{
					data[j] = -1;
					break;
				}
			}

			data[i] = -1;
			ans++;
		}

		printf("Case #%d: %d\n", kase, ans);
	}

	return 0;
}
