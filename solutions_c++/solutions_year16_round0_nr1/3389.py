#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

int solve(int n)
{
    char buf[128];
    bool visit[10] = {0};
    int seen = 0;

    for(int k = 1; k < 10000; ++ k)
    {
        sprintf(buf, "%d", k * n);
        for(char *p = buf; *p; ++ p) {
            bool &r = visit[*p - '0'];
            if(!r) seen ++;
            r = true;
        }
        if(seen == 10) {
            fprintf(stderr, "%d -> k = %d\n", n, k);
            return k * n;
        }
    }
    return -1;
}

int main() {
    int T;
    int kase = 0;
    cin >> T;
    while(T-- > 0) {
        int n; cin >> n;
        printf("Case #%d: ", ++kase);
        int t = solve(n);
        if(t < 0) printf("INSOMNIA\n");
        else printf("%d\n", t);
    }
    return 0;
}

