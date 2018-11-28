#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

typedef long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vector<double> vdouble;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define ST first
#define ND second
#define INF 1000000000
#define EPS 1e-5

int compute(int &v, int n)
{
	int out = 0;
	while(v % n == 0)
		v /= n, out++;
	return out;
}

int main()
{
	int R, N, M, K;
	
	cin >> R;
	printf("Case #1:\n");
	
	cin >> R >> N >> M >> K;
	REP(t, R)
	{
		int a, b, n = N;
		vint V(K), A(K), B(K), U(2);		
		REP(i, K)
		{
			cin >> V[i];
			if(M >= 5)
				U[0] = max(U[0], compute(V[i], 5));
			if(M >= 7)
				U[1] = max(U[1], compute(V[i], 7));
			A[i] = compute(a = V[i], 2);
			B[i] = compute(a = V[i], 3);
		}
		
		n -= (U[0] + U[1]);
		if(n)
		{
			int u = max_element(ALL(A)) - A.begin();
			int v = max_element(ALL(B)) - B.begin();
			a = A[u], b = B[v];
			if(M <= 5)
			{
				if(a + b >= n)
				{
					REP(i, 2 * (n - b) - a)
						printf("2");
					REP(i, b)
						printf("3");
					REP(i, a - (n - b))
						printf("4");
				}
				else
				{
					REP(i, n - b)
						printf("2");
					REP(i, b)
						printf("3");
				}
			}
		}
		
		REP(i, U[0])
			printf("5");
		REP(i, U[1])
			printf("7");
		puts("");
	}
	
	return 0;
}