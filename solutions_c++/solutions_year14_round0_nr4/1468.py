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
#include <algorithm>
#include <iterator>
#include <cassert>

using namespace std;

typedef long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vector<double> vdouble;
typedef vector<llong> vllong;

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

int war(vdouble &A, vdouble &B)
{
	int index = 0, out = 0;
	REP(i, SIZE(A))
	{
		while(B[index] < A[i] && index < SIZE(B))
			index++;
		if(index - i > out)
			out = index - i;
	}

	return out;
}

int deceitful_war(vdouble &A, vdouble &B)
{
	int index = 0;
	REP(i, SIZE(A) - index)
		if(A[index + i] < B[i])
			index++, i--;

	return SIZE(A) - index;
}

int main()
{
	int N;
	
	cin >> N;
	REP(t, N)
	{
		int T;
		cin >> T;
		
		vdouble A(T), B(T);
		REP(i, T)
			cin >> A[i];
		REP(i, T)
			cin >> B[i];
		sort(ALL(A)), sort(ALL(B));

		printf("Case #%d: %d %d\n", t + 1, deceitful_war(A, B), war(A, B));
	}
	
	return 0;
}