#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define int64 long long
#define Sort sort

using namespace std;

const double eps = 1e-7;

long double R[110], C[110];
long double V, X;
int N;

bool check(long double mid)
{
	long double s = 0.0;
	long double vol = 0.0;
	for (int i=0;i<N;++i)
	{
		long double nvol = min(R[i] * mid, V - vol);
		vol += nvol;
		s += nvol * C[i];
	}
	if (s > V * X + eps) return false;
	s = 0.0;
	vol = 0.0;
	for (int i=N-1;i>=0;--i)
	{
		long double nvol = min(R[i] * mid, V - vol);
		vol += nvol;
		s += nvol * C[i];
	}
	if (s < V * X - eps) return false;
	return true;
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int ii=0;ii<T;++ii)
	{
		printf("Case #%d: ", ii + 1);
		double VV, XX;
		scanf("%d %lf %lf", &N, &VV, &XX);
		V = VV;X = XX;
		//cin >> N >> V >> X;
		long double sum = 0, minR = 99999.0;;
		for (int i=0;i<N;++i)
		{
			double R0, C0;
			scanf("%lf %lf", &R0, &C0);
			R[i] = R0, C[i] = C0;
			//cin >> R[i] >> C[i];
			sum += R[i];
			minR = min(minR, R[i]);
		}
		for (int i=0;i<N;++i)
			for (int j=i+1;j<N;++j)
				if (C[i] > C[j] + eps)
				{
					swap(C[i], C[j]);
					swap(R[i], R[j]);
				}
		if (N == 1)
		{
			if (fabs(X - C[0]) < eps)
			{
				printf("%.10lf\n", (double)(V/R[0]));
			}
			else printf("IMPOSSIBLE\n");
			continue;
		}
		if (N == 2)
		{
			if (fabs(C[1] - C[0]) < eps)
			{
				if (fabs(X - C[0]) < eps)
				{
					printf("%.10lf\n", (double)(V/(R[0]+R[1])));
				}
				else
				{
					printf("IMPOSSIBLE\n");
				}
			}
			else
			{
				long double V2 = (V * X - V * C[0]) / (C[1] - C[0]);
				long double V1 = V - V2;
				if (V1 > -eps && V2 > -eps)
					printf("%.10lf\n", (double)max(V2/R[1], V1/R[0]));
				else
					printf("IMPOSSIBLE\n");
			}
			continue;
		}
		//if (ii == 15)
		//	printf(" ");
		long double l = V/sum, r = V/minR + 1.0;
		for (int itr=0;itr<6000;++itr)
		{
			long double mid = (l + r) / 2.0;
			if (check(mid)) r = mid;
			else l = mid;
		}
		check(l);
		if (l > V/minR) printf("IMPOSSIBLE\n");
		else printf("%.10lf\n", (double)l);
	}

	return 0;
}