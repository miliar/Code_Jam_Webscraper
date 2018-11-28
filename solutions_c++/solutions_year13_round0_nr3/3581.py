#include <cstdio>
#include <cstring>

int count[1001];

inline bool paap(int ab)
{
	int t = ab, ba = 0;
	while (t > 0) {
		ba = ba * 10 + t % 10;
		t /= 10;
	}
	return ab == ba;
}

inline void init()
{
	memset(count, 0, sizeof(count));
	for (int i = 1; i < 34; ++i)
		if (paap(i) && paap(i*i))
			count[i*i] = 1;
	for (int i = 1; i < 1001; ++i)
		count[i] += count[i-1];
}

int main()
{
	init();
	int cases;
	scanf("%d", &cases);
	for (int t = 1; t <= cases; ++t) {
		int a, b;
		scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", t, count[b]-count[a-1]);
	}
	return 0;
}
