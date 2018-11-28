/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 10010000;
const int M = 110;
const long long MOD = 1000000007;
const double eps = 1e-10;
int n, jj;
char out[M];

long long getVal(long long tmp, int bas){
    long long res = 0, vbas = 1;
    while (tmp) {
        long long dig = 1;
        if (tmp&1) {
            res += vbas*dig;
        }
        tmp >>= 1;
        vbas *= bas;
    }
    return res;
}

bool check(long long val){
    for (long long i = 3; i <= sqrt(val); i += 2) {
        if (val%i == 0) {
            return true;
        }
    }
    return false;
}

void printbin(long long res){
    int idx = 0;
    memset(out, 0, sizeof(out));
    while (res) {
        out[idx ++] = ((res&1)+'0');
        res >>= 1;
    }
    while (idx) {
        printf("%c",out[idx - 1]);
        -- idx;
    }
}

long long getDivsor(long long val){
    for (long long i = 3; i < val; ++ i) {
        if (val%i == 0) {
            return i;
        }
    }
    return val;
}

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/C-small-attempt0.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d",&n,&jj);
        printf("Case #%d:\n",cas);
        long long ans = 1<<(n - 1);
        int cnt = 0;
        ans |= 1;
        long long bnd = (1<<(n-2));
        for (long long i = 0; i < bnd && cnt < jj; ++ i) {
            long long v = i<<1;
            long long tmp = ans|v;
            bool isfind = true;
            for (int j = 2; j <= 10; ++ j) {
                long long res = getVal(tmp, j);
                if (!check(res)) {
                    isfind = false;
                    break;
                }
            }
            if (isfind) {
                ++ cnt;
                printbin(tmp);
           /*     puts("");
                for (int j = 2; j <= 10; ++ j) {
                    long long res = getVal(tmp, j);
                    printf(" %lld",res);
                }
                puts(""); */
                for (int j = 2; j <= 10; ++ j) {
                    long long res = getVal(tmp, j);
                    long long div = getDivsor(res);
                    printf(" %lld",div);
                }
                puts("");
            }
        }
    }
    return 0;
}