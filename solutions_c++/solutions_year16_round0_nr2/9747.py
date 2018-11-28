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

void swapPie(char str[], int s, int e) {
	int start = s;
	int end = e - 1;
	while (start < end) {
		swap(str[start], str[end]);
		++start;
		--end;
	}
	for (int i = s; i < e; ++i) {
		if (str[i] == '-') {
			str[i] = '+';
		}
		else {
			str[i] = '-';
		}
	}
}

int possibleSolution(char str[], int s, int e) {
	int cnt = 0;

	int next = e;
	while (next > 0) {
		if (str[next - 1] == '-') {
			if (str[0] == '-') {
				++cnt;
				swapPie(str, s, next);
			}
			else {
				++cnt;
				for (int i = 0; i < e; ++i) {
					if (str[i] == '+') {
						str[i] = '-';
					}
					else {
						break;
					}
				}
				++cnt;
				swapPie(str, s, next);
			}
		}
		--next;
	}

	return cnt;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("E:/in.txt", "r", stdin);
	freopen("E:/out.txt", "w", stdout);
#endif // ONLINE_JUDGE

	int testCase;
	scanf("%d", &testCase);
	int cntCase = 0;

	while (cntCase < testCase) {
		char str[105];
		scanf("%s", str);

		int len = strlen(str);
		int minCnt = possibleSolution(str, 0, len);

		printf("Case #%d: %d\n", cntCase + 1, minCnt);

		++cntCase;
	}


#ifndef ONLINE_JUDGE
	fclose(stdin);
	//    fclose( stdout );
#endif // ONLINE_JUDGE

	return 0;
}
