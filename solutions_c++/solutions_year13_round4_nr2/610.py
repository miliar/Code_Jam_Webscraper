#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T, TT;
int low[1024];
int high[1024];
int n, p, n2;

void getLowHigh(int who) {
    int r;
    int t = 0;
    for (r = 2; r <= n2; r*=2) {
        t*=2;
        if (n2 - who - 1 >= r-1)
            t+=1;
        
    }
    high[who] = n2-t;
    t = 0;
    for (r = 2; r <= n2; r*=2) {
        t*=2;
        if (who < r-1)
            t+=1;
    }
    low[who] = n2-t;
}

int main() {
    int i;
    
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%d %d", &n, &p);
        n2 = 1;
        for (i = 0; i < n; i++)
            n2*=2;
        for (i = 0; i < n2; i++) {
            getLowHigh(i);
        }
        int ans;
        for (i = 0; i < n2; i++) {
            if (low[i] <= p)
                ans = i;
        }
        printf("%d ", ans);
        for (i = 0; i < n2; i++)
            if (high[i] <= p)
                ans = i;
        printf("%d\n", ans);
        
        
    }
}