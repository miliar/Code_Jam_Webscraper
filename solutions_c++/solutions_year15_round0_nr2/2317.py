#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int n;
int P[1010];


int trial(int thold) {
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        ret += (P[i]-1)/thold;
    }
    return ret;   
}

int main() {
    int Z;
    scanf("%d", &Z);
    for (int zz = 1; zz <= Z; ++zz) {
        scanf("%d", &n);
        int mx = 0;
        for(int i = 0; i < n; ++i) {
            scanf("%d", &P[i]);
            mx = max(mx, P[i]);
        }
        
        int result = 2000000000;
        for (int t = 1; t <= mx; ++t) {
            result = min(result, t + trial(t));
        }
        
        printf("Case #%d: %d\n", zz, result);
    }
    return 0;
}
