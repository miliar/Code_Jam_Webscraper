#include <iostream>
#include <cmath>
#include <vector>
#include <climits>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define x first
#define y second

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int r, c, w;
        cin >> r >> c >> w;
        int ans = c/w + w - 1;
        if (c%w) ans += 1;
        ans *= r;
        cout << "Case #" << test << ": " << ans << endl;
    }

    return 0;
}

