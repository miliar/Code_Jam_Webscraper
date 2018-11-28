#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <string>
#include <algorithm>
#define MID(x,y) ( ( x + y ) >> 1 )
#define L(x) ( x << 1 )
#define R(x) ( x << 1 | 1 )
#define FOR(i,s,t) for(int i=(s); i<(t); i++)
#define file_r(x) freopen(x, "r", stdin)
#define file_w(x) freopen(x, "w", stdout)

using namespace std;

int main()
{
    //file_r("A-small-attempt0.in");
    file_r("A-large.in");
    file_w("output.txt");

    int T, n;
    string str;

	cin >> T;
    for (int i = 0; i < T; ++i) {
		cin >> n >> str;
        int ans = 0, val = str[0] - '0';
        for (int j = 1; j <= n; ++j) {
            if (val < j) {
                ans += j - val;
                val += j - val;
            }
            val += str[j] - '0';
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
