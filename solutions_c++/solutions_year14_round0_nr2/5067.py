#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <iomanip> 
#include <functional> 
#include <bitset> 
#include <cassert> 
#include <cmath> 
#include <ctime> 
#include <queue> 
#include <list> 
#include <memory.h> 
#include <complex> 
#include <numeric> 
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define INF ((1ll << 60) - 1) 
#define MOD 1000000007 
#define FAIL ++*(int*)0 
#define EPS 1e-11 
template<class T> T sqr(T a) {return a * a;} 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef pair<int, pii> piii; 
typedef vector<int> vi; 
typedef vector<int64> vi64; 
typedef vector<pii> vpii; 
typedef vector<vector<int> > vvi; 
typedef vector<vvi> vvvi; 
typedef vector<vector<pair<int, int > > > vvpii; 
typedef vector<vector<vector<pair<int, int > > > > vvvpii; 
typedef complex<long double> cd; 
#define TASK "hobbit" 
//---------------------------------------------------------- 

double C, F, X;

double f(int m)
{
	double t = 0;
	double dq = 2;

	for(int i = 0; i < m; ++i)
	{
		t += C / dq;
		dq += F;
	}

	t += X / dq;
	
	return t;
}

void solve()
{
	scanf("%lf%lf%lf", &C, &F, &X);

	int l = 0, r = 1 << 17;

	while(r - l > 10)
	{
		int m1 = (2 * l + r) / 3;
		int m2 = (2 * r + l) / 3;

		double t1 = f(m1);
		double t2 = f(m2);

		if(t1 < t2)
			r = m2;
		else
			l = m1;
	}

	double res = 1e20;
	for(int m = l; m < r + 1; ++m)
		res = min(res, f(m));

	printf("%.15lf\n", res);
}

int main() 
{ 
#ifndef ONLINE_JUDGE 
    freopen ("input.txt", "r", stdin); freopen ("output.txt", "w", stdout); 
#endif 
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i)
    {
    	printf("Case #%d: ", i + 1);
    	solve(); 
    }
    return 0; 
}