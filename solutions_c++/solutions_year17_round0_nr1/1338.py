#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;

int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        string s;
        int k;
        cin >> s >> k;
        int n = s.size();
        int cnt = 0;
        IFOR(i, 0, n - k) {
            if (s[i] == '-') {
                cnt++;
                FOR(j, i, i + k) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
            }
        }
        bool ok = true;
        FOR(i, 0, n) {
            if (s[i] == '-')
                ok = false;
        }
        if (!ok)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << cnt << endl;
    }
    return 0;
}