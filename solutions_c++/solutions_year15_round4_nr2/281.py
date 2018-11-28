#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

int cS;
int cL;
double V, X;
int n;
struct Water
{
	double R;
	double C;
} waters[200], S[100], L[100];

bool cmp(const Water& a, const Water& b)
{
	return a.C < b.C;
}
bool check()
{
	if(cS == 0 && L[0].C > X) return true;
	if(cL == 0 && S[cS-1].C < X) return true;
	return false;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ++ca)
	{
		cS = cL = 0;
		scanf("%d", &n);
		scanf("%lf %lf", &V, &X);
		for(int i = 0; i < n; ++i)
		{
			scanf("%lf %lf", &waters[i].R, &waters[i].C);
			if(waters[i].C < X)
				S[cS++] = waters[i];
			else
				L[cL++] = waters[i];
		}
		//
		//printf("%d %d\n", cS, cL);
		std::sort(L, L + cL, cmp);
		std::sort(S, S + cS, cmp);
		bool impossible = check();
		if(impossible)
		{
			printf("Case #%d: IMPOSSIBLE\n", ca);
			continue;
		}
		double r = 0;
		int l = 0, s = cS - 1;
		while(l < cL && fabs(L[l].C - X) < 1e-10)
			r += L[l++].R;
		while(s >= 0 && fabs(S[s].C - X) < 1e-10)
			r += S[s--].R;
		//
		//printf("%d %d\n", s, l);
		while(l < cL && s >= 0)
		{
			if(L[l].R < 1e-10) { ++l; continue; }
			if(S[s].R < 1e-10) { --s; continue; }
			double rs = L[l].C - X;
			double rl = X - S[s].C;
			double m = 1.0;
			if(rs > S[s].R)
				m = std::min(m, S[s].R / rs);
			if(rl > L[l].R)
				m = std::min(m, L[l].R / rl);
			rs *= m;
			rl *= m;
			r += rs + rl;
			S[s].R -= rs;
			L[l].R -= rl;
		}
		printf("Case #%d: %.15lf\n", ca, V / r);
	}
}
