#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void _run() {
    int a, b, k;
    cin >> a >> b >> k;
    int ans = 0;
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            if ((i & j) < k) {
                ans++;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        _run();
    }
}
