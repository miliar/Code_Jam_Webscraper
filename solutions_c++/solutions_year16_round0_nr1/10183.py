#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define MAX 202

int main()
{
	// declare
	long long N, T, R; 
	int x, n, count;
	vector<int> a(10, -1);

	// input
	//freopen("INPUT.INP", "rt", stdin);

	scanf("%d", &n);
	for (int j = 0; j < n; j++)
	{
		scanf("%lld", &N);

		if (N == 0)
		{
			printf("Case #%d: %s", j + 1, "INSOMNIA\n");
		}
		else
		{
			if (N < 0)
				N *= -1;
			
			count = 0;
			a.clear();
			a.resize(10, -1);

			for (int i = 1; count < 10; i++)
			{

				T = N * i;
				R = T;
				while (T > 0)
				{
					x = T % 10;
					T /= 10;
					if (a[x] == -1)
					{
						a[x] = x;
						count++;
					}
					if (count == 10)
					{
						printf("Case #%d: %d\n", j + 1, R);
						break;
					}
				}
			}
		}
	}
	
	return 0;
}