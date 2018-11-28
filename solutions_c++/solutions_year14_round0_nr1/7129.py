#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

void Solve(int tc)
{
	set<int> pos;

	int answer1;
	scanf("%d", &answer1);
	REP(i, 4) REP(j, 4)
	{
		int card;
		scanf("%d", &card);
		if (i + 1 == answer1) pos.insert(card);
	}

	int answer2;
	scanf("%d", &answer2);
	REP(i, 4) REP(j, 4)
	{
		int card;
		scanf("%d", &card);
		if (i + 1 != answer2 && pos.find(card) != pos.end())  pos.erase(pos.find(card));
	}

	printf("Case #%d: ", tc);

	if (pos.size() == 0) printf("Volunteer cheated!\n");
	else if (pos.size() == 1) printf("%d\n", *pos.begin());
	else printf("Bad magician!\n");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}
