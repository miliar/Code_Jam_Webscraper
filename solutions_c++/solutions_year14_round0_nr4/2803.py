#include <iostream>
#include <set>
#include <algorithm>

using namespace std;
double N[1024], K[1024];
int n;

int war() 
{
	int i;
	int j = 0;
	int lose = 0;
	for (i = 0; i < n && j < n; ++i){
		while (j < n && K[j] < N[i])
			++j;
		if (j < n) {
			++lose;
			++j;
		}
	}
	return n - lose;
}

int deceitful_war()
{
	int win = 0;
	int klow = 0, khi = n-1;
	for (int i = 0; i < n; ++i)
	{
		if (N[i] > K[klow]) {
			++win;
			klow++;
		}
		else
			khi--;
	}
	return win;
}

int main()
{
	int T;

	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &T);
	
	for (int t = 1; t<=T; ++t)
	{
		scanf("%d",&n);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &N[i]);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &K[i]);

		sort(N, N + n);
		sort(K, K + n);
		printf("Case #%d: %d %d\n", t, deceitful_war(), war());
	}
	return 0;
}
