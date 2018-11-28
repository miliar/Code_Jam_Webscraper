//darknife header
#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
#define FOD(i,n,m) for(int i = (int)n; i >= (int)m; i--)
#define EACH(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

typedef long long i64;
typedef pair<int, int> PI;

#define sz(v) ((i64)(v).size())
#define all(v) (v).begin(),(v).end()
#define bit(n) (1LL<<(i64)(n))

#define PB push_back
#define MP make_pair
#define X first
#define Y second
template<class T> void fmax(T &a, const T &b) { if (a < b) a = b; }
template<class T> void fmin(T &a, const T &b) { if (a > b) a = b; }
template<class T> T sqr(const T &a) { return a * a; }
//end darknife header
double C, F, Xi;

double aidcal(int n, double c, double f)
{
	double r = 0;

	for (int i = 0; i < n; i++)
		r += (n - i)/(2.0 + i*f);
	r *= c*f;
	return r;
}

double caltime(double c, double f, double x)
{
	double t0 = x/2.0;
//	double t1 = (x + c + c*f/2)/(2+2*f);
	double t1 = 0;
	int n = 1;
	while(1)
	{
		double tmp = aidcal(n, c, f);
		t1 = (x + tmp + c*n)/(2.0 + n*f);
		if (t0 < t1)
			return t0;
		else
		{
			t0 = t1;
			n++;
		}
	}
}

int main() {
	int Te;
	scanf("%d", &Te);
	for (int Ti = 1; Ti <= Te; Ti++) {
		cin >> C >> F >> Xi;
		double t = 0;
		t = caltime(C, F, Xi);
		printf("Case #%d: %0.7lf\n", Ti, t);

	}
	return 0;
}
