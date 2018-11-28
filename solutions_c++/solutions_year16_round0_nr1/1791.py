#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <unistd.h>
#include <cassert>
#include <memory.h>
#include <limits>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

inline string getCurDir()
{
	char cwd[1024];
	getcwd(cwd, sizeof(cwd));
	string curDir(cwd);
	cout << curDir << endl;
	return curDir + "/src/";
}

//#define SMALL
#define LARGE

int main()
{
	#ifdef SMALL
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.txt", "w+", stdout);
	#endif
	#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w+", stdout);
	#endif
	int TC;
	long N;
	bool seen[10];

	scanf("%d", &TC);
	REP(t, TC)
	{
		printf("Case #%d: ", t + 1);
		scanf("%ld", &N);
		memset(seen, false, sizeof(seen));
		if (N == 0)
		{
			puts("INSOMNIA");
			continue;
		}

		int k = 1;
		while(true)
		{
			long curNum = N * k;
			long temp = curNum;
			while (temp > 0)
			{
				seen[temp % 10] = true;
				temp = temp / 10;
			}
			//		int count;
			bool canSleep = true;
			REP(count , 10)
			{
				if (seen[count] == false)
				{
					canSleep = false;
					break;
				}
			}
			if (!canSleep)
			{
				k++;
			}
			else
			{
				printf("%ld\n", curNum);
				break;
			}
		}

	}
	return 1;
}
