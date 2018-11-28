#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
using namespace std;

const int N = 100+5;
char s[N];
int n;

int gao(int len, int sign) {
    if (len == 0) return 0;
    int cur = 0;
    if (s[len-1] == '+') {
        cur = 1;
    } else {
        cur = -1;
    }
    if (cur == sign) {
        return gao(len-1, sign);
    } else {
        return gao(len-1, -sign) + 1;
    }
}

int solve()
{
    n = strlen(s);
    return gao(n, 1);
}

int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++cas);
        scanf("%s", s);
        printf("%d\n", solve());
    }
    return 0;
}