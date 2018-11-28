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

//#define SMALL
#define LARGE

int main() {
#ifdef SMALL
	freopen("B-small-practice.in", "r", stdin);
	freopen("B-small-practice.txt", "w+", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w+", stdout);
#endif
	int TC;
	char input[100];
	char temp[100];

	scanf("%d", &TC);
	REP(t, TC)
	{
		printf("Case #%d: ", t + 1);
		scanf("%s", input);
		int res = 0;
		int lenghtInput = strlen(input)-1;
		while (true) {
			int lastBlank = -1;
			FORD(i, lenghtInput, 0)
			{
				if (input[i] == '-') {
					lastBlank = i;
					break;
				}
			}

			if (lastBlank == -1) {
				printf("%d\n", res);
				break;
			} else {
				int flipIndex = 0;
				FORD(i, lastBlank, 0) {
					if (input[i] == input[0]) {
						flipIndex = i;
						break;
					}
				}
				FORD(i, flipIndex, 0) {
					temp[i] = input[i];
				}
				FORD(i, flipIndex, 0) {
					if (temp[i] == '+') {
						input[flipIndex - i] = '-';
					} else {
						input[flipIndex - i] = '+';
					}
				}
				res++;
			}
		}

	}
	return 1;
}
