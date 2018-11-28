#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define rep2(i, j, k) for(int i = (int) j; i >= (int) k; --i)
#define ll long long
#define mp make_pair
using namespace std;

const int N = 127;
char c[N];
bool g[N];
int s[N], t;
int n;
int ans;

int main()
{
#ifdef PIT
freopen("B-large.in", "r", stdin);
freopen("B-large.out", "w", stdout);
#endif // PIT
    int T, ic = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%s", c);
        n = strlen(c);
        memset(g, 0, sizeof g);
        rep(i, 0, n) g[i] = (c[i] == '+');
        int k = 0;
        t = -1;
        memset(s, 0, sizeof s);
        if(g[n-1] == 0) s[++t] = 1;
        rep2(i, n-2, 0) {
            if(g[i] == g[i+1]) s[t]++;
            else s[++t] = 1;

        }
        printf("Case #%d: %d\n", ic++, ++t);
    }
    return 0;
}

/**
10
+-+-+-+-+-
-+-+-+-+-+-+
-
-+
+-
+++
--+-
**/
