#include <bits/stdc++.h>

const int N = 1000 + 5;
int A[N];
int n;

int work() {
    int ret = 1000;
    for (int i = 1; i <= 1000; ++ i) {
        int counter = 0;
        for (int j = 0; j < n; ++ j) {
            if (A[j] > i) {
                counter += (A[j] - i + i - 1) / i;
            }
        }
        ret = std::min(ret,i + counter);
    }
    return ret;
}

int main(int argc,char **args) {
    if (argc > 1) {
        freopen(args[1],"r",stdin);
        freopen("data.out","w",stdout);
    }
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        scanf("%d",&n);
        for (int i = 0; i < n; ++ i) {
            scanf("%d",A+i);
        }
        printf("Case #%d: %d\n",++ca,work());
    }
}
