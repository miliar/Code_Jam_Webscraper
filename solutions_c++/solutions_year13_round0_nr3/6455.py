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
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))


void proc()
{
	double r1, r2;
	LL i, res, s1, s2, rev, num, sq;
	int dig;
	cin >> r1 >> r2;
	s1 = sqrt(r1);
	s2 = sqrt(r2);
	if (s1 * s1 < r1)
	{
		s1++;
	}
	res = 0;
	for (i = s1; i <= s2 ; i++)
	{
		 num = i;
		 rev = 0;
		 while (num > 0)
		 {
			  dig = num % 10;
			  rev = rev * 10 + dig;
			  num = num / 10;
		 }
         if (i == rev)
		 {		 
			 num = sq = i*i;
			 rev = 0;
			 while (num > 0)
			 {
				  dig = num % 10;
				  rev = rev * 10 + dig;
				  num = num / 10;
			 }
			 if (sq == rev)
				res++;
		 }
	}
	static int caseNo = 0;
    cout << "Case #" << ++caseNo << ": " << res << endl;
}

int main() {
    int nCases;
    cin >> nCases;

    for (int i = 0; i < nCases; ++i) {
        proc();
    }
}
