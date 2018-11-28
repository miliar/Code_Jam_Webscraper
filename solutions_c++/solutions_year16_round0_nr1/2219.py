#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define sys_p system( "pause" )
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define sz(a) (int)a.size()

typedef long long LL;

int counts[10];
int zero_num;
void add_counts(int x) {
    while (x) {
        if (!counts[x%10])
            zero_num -= 1;
        counts[x%10] = 1;
        x /= 10;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, T_, N, i;
    scanf("%d", &T);
    FOR1(T_, T) {
        scanf("%d", &N);
        printf("Case #%d: ", T_);
        if (N == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        FOR0(i, 10)
            counts[i] = 0;
        zero_num = 10;
        i = 1;
        while(true) {
            add_counts(N*i);
            if (!zero_num)
                break;
            i += 1;
        }
        printf("%d\n", N*i);
    }
    return 0;
}