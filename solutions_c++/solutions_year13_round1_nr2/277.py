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

int main()
{
	int N;
	
	cin >> N;
	REP(t, N)
	{
		int E, R, M;
		cin >> E >> R >> M;
		R = min(E, R);
		
		vint V(M), U(M);
		REP(i, M)
			cin >> V[i];
		
		int energy = E;
		REP(i, M)
		{
			int a = max_element(V.begin() + i, V.begin() + i + min(M - i, (E + R - 1) / R)) - V.begin();
			if(i == a)
				U[i] = energy, energy = 0;
			else if(energy + R * (a - i) > E)
			{
				int b = i;
				while(b < a && V[i] >= V[b])
					b++;
				if(b == a)
				{
					int left = max(0, E - R * (a - i));
					U[i] = energy - left, energy = left;
				}
				else if(energy + R * (b - i) > E)
				{
					int left = max(0, E - R * (b - i));
					U[i] = energy - left, energy = left;
				}
			}
			
			energy = min(energy + R, E);
		}
		// REP(i, M)
			// cout << U[i] << " ";
		// cout << endl;
		
		long long out = 0;
		REP(i, M)
			out += (long long)V[i] * U[i];
		printf("Case #%d: %lld\n", t + 1, out);
	}
	
	return 0;
}