#include <algorithm>
#include <functional>
#include <vector>
#include <cstdio>
using namespace std;

int main(void)
{
	int cases;
	scanf("%i", &cases);
	for (int t = 0; t < cases; ++t)
	{
		int n;
		scanf("%i", &n);
		vector<double> naomi((size_t)n);
		vector<double> ken((size_t)n);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &naomi[i]);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &ken[i]);
		sort(naomi.begin(), naomi.end(), std::greater<double>());
		sort(ken.begin(), ken.end(), std::greater<double>());
		// Deceitful war
		int dw = 0; // Naomi
		{
			int ek = n-1;
			int en = n-1;
			for (int i = 0; i < n; ++i)
			{
				if (naomi[en] > ken[ek])
				{
					--en;
					--ek;
					++dw;
				}
				else
				{
					--en;
				}
			}
		}
		int w = 0; // Naomi
		{
			int sk = 0;
			for (int i = 0; i < n; ++i)
			{
				if (ken[sk] > naomi[i])
					++sk;
				else
					++w;
			}
		}
		printf("Case #%i: %i %i\n", t+1, dw, w);
	}
	return 0;
}
