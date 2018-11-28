#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int data[1000];
pair<int, int> indexed[1000];
int n;

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int kase = 1; kase <= T; kase++)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; i++) 
		{
			scanf("%d", data + i);
			indexed[i].first = data[i];
			indexed[i].second = i;
		}

		sort(indexed, indexed + n);

		int left = 0, right = n - 1, ans = 0;
		for(int i = 0; i < n; i++)
		{
			int cur = indexed[i].second;
			if(cur - left < right - cur)
			{
				ans += cur - left;
				left++;

				for(int j = i + 1; j < n; j++)
					if(indexed[j].second < indexed[i].second)
						indexed[j].second++;
			}
			else
			{
				ans += right - cur;
				right--;

				for(int j = i + 1; j < n; j++)
					if(indexed[j].second > indexed[i].second)
						indexed[j].second--;
			}
		}

		printf("Case #%d: %d\n", kase, ans);
	}

	return 0;
}


