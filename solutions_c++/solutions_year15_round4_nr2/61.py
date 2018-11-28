#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
using namespace std;
double R[110], C[110], V, X, ans, eps = 1e-10;
vector<pair<double, double>> a, b;
int NUM, T, n;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> NUM;
	for (int T = 1;T <= NUM;T++)
	{
		cin >> n >> V >> X;
		a.clear(), b.clear(); ans = 0;
		for (int i = 1;i <= n;i++)
		{
			scanf("%lf%lf", &R[i], &C[i]);
			if (fabs(C[i] - X) < eps) ans += R[i];
			else if (C[i] < X) a.push_back(make_pair(X - C[i], R[i]));
			else b.push_back(make_pair(C[i] - X, R[i]));
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		for (int i = 0, j = 0;i < a.size() && j < b.size();)
		{
			double t = min(a[i].second / b[j].first, b[j].second / a[i].first);
			ans += t*(a[i].first + b[j].first);
			a[i].second -= t*b[j].first;
			b[j].second -= t*a[i].first;
			if (a[i].second < eps) i++;
			if (b[j].second < eps) j++;
		}
		printf("Case #%d: ", T);
		if (ans <= 0) puts("IMPOSSIBLE");
		else printf("%.12lf\n", V / ans);
	}
	return 0;
}
