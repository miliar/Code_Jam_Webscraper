#include <cstdio>
#include <deque>
#include <algorithm>
#include <functional>
using namespace std;

int main(int argc, char const *argv[])
{
	int T, n;
	double KEN[1001], NAOMI[1001];
	int pd, pw;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%d", &n);
		pd = 0;
		pw = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%lf", &NAOMI[i]);
		}
		for (int i = 0; i < n; ++i)
		{
			scanf("%lf", &KEN[i]);
		}
		//deceitful
		deque<double> naomi(NAOMI, NAOMI + n);
		deque<double> ken(KEN, KEN + n);
		sort(naomi.begin(), naomi.end(), greater<double>());
		sort(ken.begin(), ken.end(), greater<double>());
		for (int i = 0; i < n; ++i)
		{
			if (naomi[0] > ken[0])
			{
				pd++;
				naomi.pop_front();
				ken.pop_front();
			}
			else{
				naomi.pop_back();
				ken.pop_front();
			}
		}
		//normal
		naomi =  deque<double>(NAOMI, NAOMI + n);
		ken =  deque<double>(KEN, KEN + n);
		sort(naomi.begin(), naomi.end(), greater<double>());
		sort(ken.begin(), ken.end(), greater<double>());
		for (int i = 0; i < n; ++i)
		{
			if (naomi[0] > ken[0])
			{
				pw++;
				naomi.pop_front();
				ken.pop_back();
			}
			else{
				deque<double>::iterator ant = ken.begin();
				deque<double>::iterator it = ken.begin();
				while (it != ken.end() && *it > naomi[0])
				{
					ant = it;
					it++;
				}
				ken.erase(ant);
				naomi.pop_front();
			}
		}

		printf("Case #%d: %d %d\n", t, pd, pw);
	}
	return 0;
}