#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
#include <complex>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef complex<double> cpx;
const int INF = numeric_limits<int>::max();

double EPS = 1e-9;
double p[300];
double cp[300];
int n, c;

cpx EXP(double t)
{
	double theta = t * 2 * M_PI / (c + 1);
	return cpx(cos(theta),sin(theta));
}

double tieprob_slow()
{
	double r = 0;
	for(int m=0;m<(1<<c);m++)
	{
		if(__builtin_popcount(m) != c/2)
			continue;
		double x=1;
		for(int i=0;i<c;i++)
			if((m>>i)&1)
				x*=cp[i];
			else
				x*=(1-cp[i]);
		r += x;
	}
	return r;
}

double tieprob()
{
	cpx r = 0;
	for(int k=0;k<=c;k++)
	{
		cpx q = EXP(-k * c/2);
		for(int i=0;i<c;i++)
			q *= cpx(1) + (EXP(k) - cpx(1)) * cp[i];
		r += q;
	}
	r /= (c+1);
	assert(imag(r) < EPS);
	double rr = abs(r);
/*
	double check = tieprob_slow();
	if (abs(rr - check) > EPS)
	{
		printf("%.9f %.9f\n", rr, check);
		assert(false);
	}
*/
	return rr;
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		scanf("%d%d", &n, &c);
		for(int i=0;i<n;i++)
			scanf("%lf", p+i);
		sort(p, p+n);
//		for(int i=0;i<n;i++) printf("%.2f ", p[i]); printf("\n");

		double a = 0;
		for(int k=0;k<c;k++)
		{
			int j=0;
			for(int i=0;i<k;i++)
				cp[j++]=p[n-1-i];
			for(int i=k;i<c;i++)
				cp[j++]=p[i-k];
			a = max(a, tieprob());
		}
		{
			for(int i=0;i<c;i++)
				cp[i]=p[i];
			a = max(a, tieprob());
		}
		{
			for(int i=0;i<c;i++)
				cp[i]=p[n-1-i];
			a = max(a, tieprob());
		}
/*
		for(int m=0;m<(1<<n);m++)
		{
			if(__builtin_popcount(m) != c)
				continue;
			int j=0;
			for(int i=0;i<n;i++)
				if((m>>i)&1)
					cp[j++] = p[i];
			double aa = tieprob();
			if(aa > a + EPS)
			{
				for(int i=0;i<c;i++) printf("%.2f ", cp[i]); printf("\n");
				printf("%f %f\n", a, aa);				exit(0);
				//a = aa;
			}
		}
*/
		printf("Case #%d: %.9f\n", test_case, a);
	}
	return 0;
}
