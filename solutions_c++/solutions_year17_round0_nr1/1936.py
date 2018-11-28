#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;

int T, K, cas = 1;
string s;
int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        cin >> s;
        scanf("%d", &K);
        int cnt = 0;
        for (int i = 0; i + K <= s.length(); i++)
            if (s[i] == '-') {
                cnt++;
                for (int j = i; j < i + K; j++)
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
            }
        bool flag = true;
        for (int i = s.length() - K + 1; i < s.length(); i++)
            if (s[i] == '-') {
                flag = false;
                break;
            }
        if (flag) printf("Case #%d: %d\n", cas, cnt);
        else printf("Case #%d: IMPOSSIBLE\n", cas);
        cas++;
    }
    return 0;
}