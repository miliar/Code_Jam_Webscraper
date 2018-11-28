#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N;
double naomi[100], ken[100];
double memo[100][2048];

int dp(int idx, int mask) {
    if(idx == N) return 0;
    if(memo[idx][mask] != -1) return memo[idx][mask];
    int best = -(1<<10);
    for(int i = 0; i < N; i++) {
        if(mask & (1<<i)) continue;
        int can = ((naomi[idx] < ken[i]) ? 0:1);
        best = max(best,max(dp(idx+1, mask|(1<<i)) + can,\
                dp(idx+1,mask)));
    }
    return memo[idx][mask] = best;
}

int main() {
    int T;
    scanf("%d", &T);
for(int kase = 1; kase <= T; kase++) {
    scanf("%d", &N);
    for(int i = 0; i < 100; i++)
        for(int j = 0; j < 2048; j++)
            memo[i][j] = -1;
    int war = 0;
    for(int i = 0; i < N; i++)
        scanf("%lf", &naomi[i]);
    for(int i = 0; i < N; i++)
        scanf("%lf", &ken[i]);
    vector<double> wnaomi(naomi,naomi+N);
    vector<double> wken(ken,ken+N);
    sort(wnaomi.begin(),wnaomi.end());
    sort(wken.begin(),wken.end());
    for(int i = N-1; i >= 0; i--) {
        vector<double>::iterator up;
        up = lower_bound(wken.begin(),wken.end(),*(wnaomi.end()-1));
        if(up == wken.end()) {
            war++;
            wnaomi.erase(wnaomi.end()-1);
            wken.erase(wken.begin());
        } else {
            wnaomi.erase(wnaomi.end()-1);
            wken.erase(up);
        }
    }
    printf("Case #%d: %d %d\n",kase, dp(0,0), war);
}
    return 0;
}
