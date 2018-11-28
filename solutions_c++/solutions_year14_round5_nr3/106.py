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
#include <cassert>
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

const int MAX = 2007;
int N;
pair<int, bool> ids[MAX];

bool seen[MAX], inside[MAX], seen2[MAX];
int last[MAX];

void Solve(int tc)
{
	scanf("%d", &N);
	REP(i, N)
	{
		char action;
		int id;
		scanf(" %c %d", &action, &id);
		ids[i] = make_pair(id, action=='E');
	}
	bool ok = true;
	memset(last, -1, sizeof(last));
	memset(seen, 0, sizeof(seen));
	memset(inside, 0, sizeof(inside));
	REP(i, N)
	{
		int id = ids[i].first;
		bool enter = ids[i].second;
		if (!id) continue;

		if (enter)
		{
			if (inside[id])
			{
				int found = -1;
				FORD(j, i-1, 0)
				{
					if (ids[j].first == 0 && ids[j].second == false)
						found = j;
					if (ids[j].first == id)
					{
						assert(ids[j].second == true);
						break;
					}
				}
				if (found == -1)
				{
					ok = false;
					goto DONE;
				}
				ids[found].first = id;
			}
			else
				inside[id] = true;
		}
		else // leave
		{
			if (inside[id])
				inside[id] = false;
			else if (seen[id])
			{
				int found = -1;
				FORD(j, i-1, 0)
				{
					if (ids[j].first == 0 && ids[j].second == true)
						found = j;
					if (ids[j].first == id)
					{
						assert(ids[j].second == false);
						break;
					}
				}
				if (found == -1)
				{
					ok = false;
					goto DONE;
				}
				ids[found].first = id;
			}
		}
		seen[id] = true;
		last[id] = i;
	}

DONE: 
	;

	printf("Case #%d: ", tc);
	if (!ok)
	{
		printf("CRIME TIME\n");
		return;
	}

	REP(i, N)
	{
		int id = ids[i].first;
		if (!id || !inside[id] || last[id] != i) continue;
		assert(ids[i].second == true);
		FOR(j, i+1, N-1)
			if (ids[j].first == 0 && ids[j].second == false)
			{
				ids[j].first = id;
				break;
			}
	}

	memset(inside, 0, sizeof(inside));
	memset(seen, 0, sizeof(seen));
	int result = 0, masked = 0;
	REP(i, N)
	{
		int id = ids[i].first;
		bool enter = ids[i].second;

		if (id == 0)
		{
			if (enter)
			{
				++result;
				++masked;
			}
			else
			{
				if (masked)
				{
					--result;
					--masked;
				}
				else
				{
					memset(seen2, 0, sizeof(seen2));
					int found = -1;
					FOR(j, i+1, N-1)
					{
						if (ids[j].first)
							seen2[ids[j].first] = true;
						else if (ids[j].second == true)
						{
							found = j;
							break;
						}
					}
					REP(j, MAX)
						if (inside[j] && !seen2[j])
						{
							ids[found].first = j;
							--result;
							break;
						}
				}
			}
		}
		else
		{
			if (enter)
			{
				assert(inside[id] == false);
				result += 1;
				inside[id] = true;
			}
			else // leave
			{
				if (inside[id])
				{
					result -= 1;
					inside[id] = false;
				}
				else
				{
					assert(seen[id] == false);
					if (masked)
					{
						--masked;
						--result;
					}
				}
			}
			seen[id] = true;
		}
	}
	printf("%d\n", result);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}