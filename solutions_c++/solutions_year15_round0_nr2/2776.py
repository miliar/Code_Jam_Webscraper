#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

int p[1010];

void solve(int ca){
    int n, mp = 0;
    scanf("%d",&n);

    for (int i = 0; i < n; i++){
        scanf("%d",&p[i]);
        mp = max(mp, p[i]);
    }

    int ans = 1000;

    for (int l = 1; l <= mp; l++){
        int temp = l;
        for (int i = 0; i < n; i++){
            temp += ceil( (p[i] + 0.0) / l) - 1;
        }
        ans = min(temp, ans);
    }
    printf("Case #%d: %d\n", ca, ans);
}

int main(){
    int T;
    scanf("%d",&T);
    for (int ca = 1; ca <= T; ca++){
        solve(ca);
    }
}
