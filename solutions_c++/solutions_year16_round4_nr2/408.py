#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <thread>

using namespace std;

#define ll long long


double mem[1<<16][10];
double P[201];
int N, K;

double solve(int used, int left, int pos) {
    if (left < 0) return 0.0;
    double& ans = mem[used][left];
    if (ans > -0.5) return ans;
    
    while (!(used & (1<<pos)) && pos < N) pos++;
    if (pos >= N) {
        return ans = (left == 0) ? 1.0 : 0.0;
    }

    used ^= (1<<pos);
    double p = P[pos];
    return ans = p * solve(used, left-1, pos+1) + (1-p) * solve(used, left, pos+1);
}

double mem2[201][201][201];
double solve2(int l, int r, int t) {
    if (t < 0) return 0.0;

    double &ans = mem2[l][r][t];
    if (ans > -0.5) return ans;

    if (l > 0) {
        double p = P[l - 1];
        ans = p * solve2(l-1, r, t-1) + (1-p) * solve2(l-1, r, t);
    } else if (r > 0) {
        double p = P[N-r];
        ans = p * solve2(l, r-1, t-1) + (1-p) * solve2(l, r-1, t);
    } else {
        ans =(t == 0) ? 1.0 : 0.0;
    }
    //printf("%d %d %d gives %.2f\n", l, r, t, ans);
    return ans;
}

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        memset(mem,-2,sizeof(mem));
        memset(mem2,-2,sizeof(mem2));
        cin>>N>>K;

        for (int i=0;i<N;++i) {
            cin>>P[i];
        }
        sort(P, P+N);

        /*
        double ans = -100;
        int best = 0;
        for (int i=0;i<(1<<N);++i) {
            int cnt = 0;
            for (int j=0;j<N;++j) {
                if (i & (1<<j)) {
                    ++cnt;
                }
            }
            if (cnt != K) {
                continue;
            }
            double cur = solve(i, K/2, 0);
            if (cur > ans) {
                ans = cur;
                best = i;
            }
        }
        */

        double ans2 = -100;
        for (int i=0;i<=K;++i) {
            ans2 = max(ans2, solve2(i, K-i, K/2)); 
        }

        

        printf("Case #%d: %.9f\n", t, ans2);
        /*
        for (int i=0;i<N;++i) {
            if (best & (1<<i)) {
                printf("%d (%.2f) ", i, P[i]);
            }
        }
        printf("\n");
        */
    }
}
