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
const int N = 80100;
const int M = 100;
const long long MOD = 1000000007;
const double eps = 1e-10;
bool vis[M];
int cnt;
long long n;

void countdig(long long val){
    while (val && cnt < 10) {
        int v = val%10;
        val /= 10;
        if (!vis[v]) {
            vis[v] = 1;
            ++ cnt;
        }
    }
}

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/A-large.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
    /*    for (long long i = 0; i <= 1000001; ++ i) {
            printf("%lld : ",i);
            if (!i) {
                printf("INSOMNIA\n");
            }else{
             //   bool isfind = false;
                cnt = 0;
                memset(vis, 0, sizeof(vis));
                for (long long j = 1; j <= 100; ++ j) {
                    long long val = j*i;
                    countdig(val);
                    if (cnt >= 10) {
                        printf("%lld\n",val);
                        break;
                    }
                }
                if (cnt < 10) {
                    printf("%lld : INSOMNIA\n",i);
                }
            }
        }*/
        scanf("%lld",&n);
        printf("Case #%d: ",cas);
        if (!n) {
            puts("INSOMNIA");
        } else {
            cnt = 0;
            memset(vis, 0, sizeof(vis));
            for (long long j = 1; j <= 100; ++ j) {
                countdig(j*n);
                if (cnt >= 10) {
                    printf("%lld\n",j*n);
                    break;
                }
            }
        }
    }
    return 0;
}