
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int solve(int n);

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int icase;
    scanf("%d", &icase);
    for(int i=1; i<=icase; ++i) {
        int n;
        scanf("%d", &n);
        int ans = solve(n);
        printf("Case #%d: ", i);
        if(-1 != ans) {
            printf("%d\n", ans);
        }
        else {
            printf("INSOMNIA\n");
        }
    }
    /*
    for(int i=0; i<1000000; ++i) {
        int ans = solve(i);
        if(-1 == ans) {
            printf("%d\n", i);
        }
        //printf("i=%d ans:=%d\n", i, solve(i));
    }
    */
    return 0;
}

int solve(int n) {
    int ia[10], ans = -1;
    memset(ia, 0, sizeof(ia));
    for(int i=1; i<100; ++i) {
        int m = i * n;
//        printf("%d\n", m);
        while(m) {
            int b = m % 10;
            m /= 10;
            if(0 == ia[b]) { ia[b] = 1; }
        }
        bool tag = true;
        for(int j=0; j<10; ++j) {
            if(0 == ia[j]) {
                tag = false;
                break;
            }
        }
        if(tag) {
            ans = i*n;
            break;
        }
    }
    return ans;
}

/*
1 1/2/3/4/5/6/7/8/9/10
2 90
3 3/6/9/12/15/18/21/24/27/30
4 4/8/12/16/20/24/28/32/36/40/44/48/52/72/92
*/
