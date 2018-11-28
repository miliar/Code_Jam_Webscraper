#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int main() {
    int i, j, t, sum, n;
    char c;
    scanf("%d", &t);
    for(j = 1; j <= t; ++j) {
        scanf("%d", &n);
        getchar();
        int f = 0, count = 0;
        for(i = 0; i <= n; ++i) {
            c = getchar();
            int dig = c - '0';
            if(f < i) {
                count += (i - f);
                f = i;
            }
            f += dig;
        }
        printf("Case #%d: %d\n", j, count);
    }
    return 0;
}

