#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

int main(int argc, char** argv)
{
	int T, N, m[10001];
	int x,y,z, max;
	int v;
	scanf("%d", &T);
	for (x = 1; x <= T; ++x)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &m[i]);
		}

		// first method
		max = 0;
		y = 0;
		for (int i = 1; i < N; ++i)
		{
			if (m[i-1] > m[i])
			{
				v = m[i-1] - m[i];
				y += v;
				if (v > max)
				{
					max = v;
				}
			}
		}

		// second method
		z = 0;
		for (int i = 0; i < N-1; ++i)
		{
			z += std::min(m[i], max);
		}
		printf("Case #%d: %d %d\n", x, y, z);
	}
}