#include <stdio.h>
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;


int doit()
{
	int n;
	scanf("%d", &n);
	vector<int> ps(n);
	std::for_each(ps.begin(), ps.end(), [](int &x) { scanf("%d", &x); });
	int ret = *std::max_element(ps.begin(), ps.end());
	for (int max_per_plate = 1; max_per_plate < ret; ++max_per_plate)
	{
		int ret2 = max_per_plate + std::accumulate(ps.begin(), ps.end(), 0,
				[max_per_plate](int acc, const int &x)
				{
					return acc + (x - 1) / max_per_plate;
				}
		);
		if (ret2 < ret)
			ret = ret2;
	}
	return ret;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int ret = doit();
		printf("Case #%d: %d\n", i+1, ret);
	}
	return 0;
}
