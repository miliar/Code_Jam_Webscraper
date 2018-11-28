#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <bitset>
#include <string>
#include <cstring>
#include <limits.h>
#include <ctime>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

using namespace std;

typedef unsigned long long int              ULLN;
typedef long long int                       LLN;
typedef unsigned int                        UINT;
typedef vector<int>                         VI;
typedef vector<double>                      VD;
typedef vector<vector<int> >                VVI;
typedef vector<string>                      VS;
typedef vector<vector<string> >             VVS;
typedef set<int>                            SI;
typedef set<string>                         SS;
typedef map<int, int>                       MII;

#define ONLINE_JUDGE_NO

int main()
{

#ifndef ONLINE_JUDGE
	freopen("E:/in.txt", "r", stdin);
	freopen("E:/out.txt", "w", stdout);
#endif // ONLINE_JUDGE

	int T;
	scanf("%d", &T);
	int testCase = 0;

	while (testCase < T) {
		int N;
		scanf("%d", &N);

		if (N != 0) {
			bool seen[10];
			memset(seen, false, sizeof(seen));
			
			int seenCnt = 0;
			LLN nextN = 0;

			while (seenCnt < 10) {
				nextN += N;

				LLN cpyNext = nextN;
				while (cpyNext) {
					int tmp = cpyNext % 10;
					if (!seen[tmp]) {
						seen[tmp] = true;
						++seenCnt;
					}
					cpyNext /= 10;
				}
			}

			printf("Case #%d: %d\n", testCase + 1, nextN);
		}
		else {
			printf("Case #%d: INSOMNIA\n", testCase + 1);
		}

		++testCase;
	}

#ifndef ONLINE_JUDGE
	fclose(stdin);
	//    fclose( stdout );
#endif // ONLINE_JUDGE

	return 0;
}
