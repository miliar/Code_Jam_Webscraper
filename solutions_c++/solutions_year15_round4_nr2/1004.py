#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

typedef long long int64;
const int inf = (int)1.05e9;
const double eps = 1e-8;


bool is_ok(const double t, const double v, const double x, const vector<pair<double, double> > &crs)
{
	double total_water = 0;
	const int n = crs.size();

	for(int i = 0; i < n; ++i)
		total_water += crs[i].second * t;

	if(total_water < v)
		return false;

	double hi_karory = 0;
	double lo_karory = 0;
	// feng the 8th project;

	double remain;

	remain = v;
	for(int i = 0; i < n; ++i) {
		const double c = crs[i].first;
		const double r = crs[i].second;
		if(remain > r * t) {
			lo_karory += c * r * t;
			remain -= r * t;
		} else if(remain > 0) {
			lo_karory += c * remain;
			remain = 0;
		}
	}

	remain = v;
	for(int i = n - 1; i >= 0; --i) {
		const double c = crs[i].first;
		const double r = crs[i].second;
		if(remain > r * t) {
			hi_karory += c * r * t;
			remain -= r * t;
		} else if(remain > 0) {
			hi_karory += c * remain;
			remain = 0;
		}
	}

	bool ok = lo_karory < x * v + eps && x * v < hi_karory + eps;

	return ok;
}


int main()
{
	const int max_step = 100000;
	int test_case;

	scanf("%d", &test_case);

	for(int case_num = 1; case_num <= test_case; ++case_num) {

		int n;
		double v, x;
		double r_min = 1000000;
		vector<pair<double, double> > crs;

		scanf("%d%lf%lf", &n, &v, &x);
		crs.resize(n);
		for(int i = 0; i < n; ++i) {
			scanf("%lf%lf", &crs[i].second, &crs[i].first);
			r_min = min(r_min, crs[i].second);
		}
		sort(crs.begin(), crs.end());

		if(n == 1) {
			if(x != crs[0].first)
				printf("Case #%d: IMPOSSIBLE\n", case_num);
			else
				printf("Case #%d: %.30lf\n", case_num, v / crs[0].second);
			continue;
		}

		if(crs[0].first > x || crs[1].first < x) {
			printf("Case #%d: IMPOSSIBLE\n", case_num);
			continue;
		}

		if(crs[0].first == x || crs[1].first == x) {
			if(crs[0].first == crs[1].first) {
				printf("Case #%d: %.30lf\n", case_num, v / (crs[0].second + crs[1].second));
			} else if(crs[0].first == x) {
				printf("Case #%d: %.30lf\n", case_num, v / crs[0].second);
			} else {
				printf("Case #%d: %.30lf\n", case_num, v / crs[1].second);
			}
			continue;
		}

		double ddd  =crs[1].first - crs[0].first;
		double uv = (x - crs[0].first) / ddd * v;
		double lv = (crs[1].first - x) / ddd * v;

		double ans = max(uv / crs[1].second, lv / crs[0].second);

		printf("Case #%d: %.30lf\n", case_num, ans);
	}

	return 0;
}
