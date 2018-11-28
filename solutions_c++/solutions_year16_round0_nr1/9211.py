#include <bits/stdc++.h>
using namespace std;
int d[10];
bool chk() {
    for (int i=0; i<10; i++) if (d[i] == 0) return false;
    return true;
}
int main() {
    int T,N;
    scanf("%d",&T);
    for (int tt=1; tt<=T; tt++) {
        memset(d,0,sizeof d);
        scanf("%d",&N);
        printf("Case #%d: ",tt);
        if (N == 0) {printf("INSOMNIA\n"); continue;}
        int n = 0;
        while (!chk()) {
            n += N;
            int t = n;
            while (t > 0) {
                d[t%10]++;
                t/=10;
            }
        }
        printf("%d\n",n);
    }
}
