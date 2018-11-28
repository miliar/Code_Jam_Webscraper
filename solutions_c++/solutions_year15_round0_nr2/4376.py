#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int b[2000],a[2000];

int rec(int mx, int lvl) {
    if(lvl > mx) return mx;
    int M;
    int ret = mx;
    for(int i=1000;i>=1;i--) if(b[i]!=0) {
            M = i;
            if(M<=3) return M;
            for(int j=2;j<=4;j++) {
                b[i] --;
                b[i/j] += i/j - i%j;
                b[i/j+1] += i%j;
                ret = min(ret, rec(mx, lvl+1)+j-1);
                b[i/j] -= (i/j - i%j);
                b[i/j+1] -= i%j;
                b[i] ++;
            }
            break;
    }
    //int ret = rec(mx, lvl+1);
    return min(ret, M);
}

int main() {
    int n, T;
    freopen("A.txt", "r", stdin);
    freopen("A_out.txt", "w", stdout);
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++) {
        scanf("%d",&n);
        int mx = -1;
        memset(b,0,sizeof b);
        for(int i=0;i<n;i++) {
            scanf("%d",&a[i]);
            b[a[i]] ++;
            mx = max(mx, a[i]);
        }
        printf("Case #%d: %d\n",cs, rec(mx, 0));
        //printf("Case #%d: %d\n", cs,rec(mx, 0));
    }
}
