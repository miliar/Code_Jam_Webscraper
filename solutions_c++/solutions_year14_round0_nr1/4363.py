#include<cstdio>
#include<algorithm>
using namespace std;
int a[23][23],b[23][23],t0,t1,sTT,u[23];
int main() {
    int TT = 1;
    for (scanf("%d", &sTT); TT <= sTT; ++TT) {
        printf("Case #%d: ", TT);
        scanf("%d", &t0);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j) scanf("%d", a[i] + j);
        scanf("%d", &t1);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j) scanf("%d", b[i] + j);
        fill(u, u + 17, 0);
        for (int i = 1; i <= 4; ++i) ++ u[a[t0][i]], ++ u[b[t1][i]];
        int k = 0;
        for (int i = 1; i <= 16; ++i) 
            if (u[i] == 2) k = k == 0 ? i : -1;
        if (k > 0) printf("%d\n", k);
        else if (k < 0) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
