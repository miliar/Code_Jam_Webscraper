#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 1 << 10;

int n;
char s[nmax];

void readTest() {
	scanf("%d", &n);
	scanf("%s", s);
}

void solveTest() {
	int x = 0;
	int c = s[0] - '0';
	for(int i = 1; i <= n; ++i) {
		if (i > c) {
			x = max(x, i - c);
		}
		c += s[i] - '0';
	}
	printf("%d\n", x);
}

int main()
{
    freopen("A.in", "rt", stdin);

    bool submit = 1;

    if (submit) {
        freopen("A.out", "wt", stdout);
    }

    int t;
    scanf("%d", &t);
    for(int tt = 0; tt < t; ++tt) {
        readTest();
        printf("Case #%d: ", tt + 1);
        solveTest();
        if (submit) {
            cerr << "Case " << tt + 1 << " done\n";
        }
    }
    cerr << "Finished" << endl;
    return 0;
}
