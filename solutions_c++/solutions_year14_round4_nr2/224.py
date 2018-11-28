#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <algorithm>
#define MAXN 1005

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static pair<int, int> data[MAXN];
	static int a[MAXN];
	for (iT = 0; iT < T; iT++)
	{
		int N;
		scanf("%d",&N);
		int i;
		for (i = 0; i < N; i++)
		{
			scanf("%d",&(data[i].first));
			data[i].second = i;
		}
		sort(data,data+N);
		for (i = 0; i < N; i++) data[i].first = i;
		for (i = 0; i < N; i++)
		{
			int temp = data[i].first; data[i].first = data[i].second; data[i].second = temp;
		}
		sort(data,data+N);
		for (i = 0; i < N; i++) a[i] = data[i].second;
		int res = 0;

		int pos, j, cnt1, cnt2;
		for (i = 0; i < N; i++)
		{
			pos = 0;
			while (a[pos] != i) pos++;
			
			cnt1 = 0;
			for (j = pos-1; j >= 0; j--)
			{
				if (a[j] > i) cnt1++;
			}

			cnt2 = 0;
			for (j = pos+1; j < N; j++)
			{
				if (a[j] > i) cnt2++;
			}

			if (cnt1 < cnt2) res += cnt1;
			else res += cnt2;
		}

		printf("Case #%d: %d\n",iT+1,res);
	}
	return 0;
}
