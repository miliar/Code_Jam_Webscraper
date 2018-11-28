#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

typedef long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vector<double> vdouble;
typedef vector<llong> vllong;
typedef set<int> sint;

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
#define INFL 1000000000000000000LL
#define EPS 1e-5

void pick(vint &A)
{
	int n, a;

	cin >> n;
	REP(i, 4 * (n - 1))
		cin >> a;
	REP(i, 4)
		cin >> A[i];
	REP(i, 4 * (4 - n))
		cin >> a;
	sort(ALL(A));
}

int main()
{
	int N;
	
	cin >> N;
	REP(t, N)
	{
		vint A(4), B(4), C(4);
		pick(A), pick(B);
		
		
		int out = set_intersection(ALL(A), ALL(B), C.begin()) - C.begin();
		if(out == 0)
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		else if(out == 1)
			printf("Case #%d: %d\n", t + 1, C[0]);
		else
			printf("Case #%d: Bad magician!\n", t + 1);
	}
	
	return 0;
}