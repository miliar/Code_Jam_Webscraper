#pragma ide diagnostic ignored "OCUnusedMacroInspection"
#pragma ide diagnostic ignored "UnusedImportStatement"
#define _USE_MATH_DEFINES

#define TASK A

#define forn(i, a, b) for (int i = (a); i < (b); i++)
#define INF int(1e9)
#define EPS 1e-9

#define int64 long long
#define uint64 unsigned long long
#define var auto
#define mp make_pair

#define A first
#define B second

#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>
#include <cstdlib>
#include <stack>
#include <list>
#include <ctime>

using namespace std;

int main(int argc, const char * argv[]) {
#ifdef MISTMAC
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    forn (i, 0, t) {
        int n;
        cin >> n;

        string s;
        cin >> s;

        int friendsCount = 0;
        int standCount = 0;
        forn (j, 0, n + 1) {
            if (standCount < j) {
                friendsCount += j - standCount;
                standCount = j;
            }
            standCount += s[j] - '0';
        }
        printf("Case #%d: %d\n", i + 1, friendsCount);
    }
    return 0;
}