#define _CRT_SECURE_NO_WARNINGS

#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("in.txt", "rb", stdin);
	freopen("out.txt", "wb", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);

		int N;

		scanf("%d", &N);

		if (N == 0)
		{
			printf("INSOMNIA\n");
		}
		else
		{
			int cnt = 0;

			bool p[10];
			memset(p, 0, sizeof(p));

			long long m = 0;

			while (cnt < 10)
			{
				m += N;

				assert(m > 0);

				long long q = m;

				while (q != 0)
				{
					int d = q % 10;
					q /= 10;

					if (!p[d])
					{
						p[d] = true;

						cnt++;
					}
				}
			}

			printf("%lld\n", m);
		}
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
