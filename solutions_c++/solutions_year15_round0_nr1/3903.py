#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <math.h>
#include <algorithm>

using namespace std;

string s;
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int kase = 0;
    cin >> kase;
    for(int k = 1; k <= kase; k++) {
        int len;
        cin >> len >> s;
        int ans = 0, sum = 0;
        for(int i = 0; i <= len; i++) {
            if(sum < i && s[i] != '0') {
                int t = i - sum;
                ans += t;
                sum += t;
            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
