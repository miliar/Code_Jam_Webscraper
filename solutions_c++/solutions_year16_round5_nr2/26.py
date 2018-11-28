#include <cstdio>
#include <algorithm>
#include <numeric>
#include <cstring>
#include <vector>
#include <stack>
#include <ctime>
#include <cstdlib>
#include <cstring>
using namespace std;

int p[100];
char s[101], t[20];

void preprocess(int) {
}

bool v[100], r[100];
bool sample(int n) {
    fill_n(v, n, false);
    char s2[101];
    for(int i = 0; i < n; i++) {
        int j = rand() % (n - i), x = 0;
        for(int k = 0; k < n; k++)
            if(!v[k] && j-- == 0) {
                x = k;
                break;
            }
        while(p[x] && !v[p[x] - 1])
            x = p[x] - 1;
        v[x] = true;
        s2[i] = s[x];
    }
    s2[n] = '\0';
    return strstr(s2, t);
}

double solve(int n) {
    int ans = 0;
    for(int i = 0; i < 10000; i++)
        if(sample(n))
            ans++;
    return ans / 10000.0;
}

int main() {
    srand(time(nullptr));
    int ttt;
    scanf("%d", &ttt);
    for(int tt = 1; tt <= ttt; tt++) {
        fprintf(stderr, "%d\n", tt);
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%d", p + i);
        scanf("%s", s);
        preprocess(n);
        int m;
        scanf("%d", &m);
        printf("Case #%d:", tt);
        for(int i = 0; i < m; i++) {
            scanf("%s", t);
            printf(" %f", solve(n));
        }
        putchar('\n');
    }
}

