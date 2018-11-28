#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long
#define Max

using namespace std;

ll gcd(ll a, ll b ) {
    return !b ? a : gcd(b , a % b);
}

int pow2(ll N) {
    return (N&(N - 1)) == 0;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, N, X, files[10002];
    cin >> T;
    for(int cas = 1; cas <= T; cas ++) {
        cin >> N >> X;
        for(int i = 0; i < N; i++) {
            cin >> files[i];
        }
        sort(files, files + N);
        int L = 0, R = N - 1, ret = 0;
        while( L <= R) {
            if( files[L] + files[R] <= X) {
                ret ++;
                L ++;
                R --;
            } else {
                ret ++;
                R --;
            }
        }
        printf("Case #%d: %d\n", cas, ret);
    }

    return 0;
}
