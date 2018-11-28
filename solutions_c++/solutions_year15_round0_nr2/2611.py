# include <iostream>
# include <cstdio>
# include <cstring>

using namespace std;

int c[1200];
int M, ans;

void calc() {
    ans = ~0U>>1;
    for(int i = M; i; --i) {
        int tmp = i;
        for(int j = i + 1; j <= M; ++j) 
            tmp += (j - 1) / i * c[j];
        ans = min(ans, tmp);
    }
}

int main() {
    int T; cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        int n; scanf("%d", &n);
        for(int i = 0; i < 1000; ++i) c[i] = 0;
        int x; M = 0;
        for(int i = 0; i < n; ++i) {
            scanf("%d", &x);
            M = max(M, x);
            c[x] += 1;
        }
        calc();
        printf("Case #%d: %d\n", cas, ans);
    }
}

