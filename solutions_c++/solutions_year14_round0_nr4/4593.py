#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <float.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> naomi, ken;
int n_case, ans1, ans2;

bool decrease(const double &a, const double &b)
{
	return a > b;
}

void solve_2()
{
	vector<double> na = naomi, ke = ken;

	sort(na.begin(), na.end(), decrease);
	sort(ke.begin(), ke.end(), decrease);

	for (int i = 0; i < na.size(); i++)
	{
		//printf("%f VS. %f\n", na[i], ke.front());
		if (ke.front() > na[i])
			ke.erase(ke.begin());
		else
		{
			ke.pop_back();
			ans2++;
		}
	}
}

void solve_1()
{
	vector<double> na = naomi, ke = ken;

	sort(na.begin(), na.end(), decrease);
	sort(ke.begin(), ke.end(), decrease);

	for (int i = 0; i < ke.size(); i++)
	{
		//printf("%f VS. %f\n", ke[i], na.front());
		if (na.front() > ke[i])
		{
			na.erase(na.begin());
			ans1++;
		}
		else
			na.pop_back();
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	while(scanf("%d", &n_case) != EOF)
	{
		for (int t = 0; t < n_case; t++)
		{
			/// init
			naomi.clear();
			ken.clear();
			ans1 = ans2 = 0;
			/// read
			int cnt;
			scanf("%d", &cnt);
			naomi.resize(cnt);
			ken.resize(cnt);
			for (int i = 0; i < cnt; i++) scanf("%lf", &naomi[i]);
			for (int i = 0; i < cnt; i++) scanf("%lf", &ken[i]);
			/// calc
			solve_1();
			solve_2();
			/// output
			printf("Case #%d: %d %d\n", t+1, ans1, ans2);
		}
	}

	return 0;
}
