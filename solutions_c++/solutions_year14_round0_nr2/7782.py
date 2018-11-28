#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int task;
	scanf("%d", &task);
	for (int _i = 1; _i <= task; ++_i)
	{
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		int pred = max(int((f * x - 2 * c) / (f * c)), 0);
		double p = 2., t = 0;
		for (int i = 0; i < pred; ++i)
		{
			t += c / p, p += f;
			if (c / p * (pred - i) < 1e-8) break;
		}
		printf("Case #%d: %.10lf\n", _i, t + x / p);
		//printf("predict : %d\n", max(pred, 0));
		/*
		p = 2., t = 0;
		for (int i = 0; i <= pred + 5; ++i)
			printf("%d: %.6lf\n", i, t + x / p), t += c / p, p += f;*/
	}

	return 0;
}