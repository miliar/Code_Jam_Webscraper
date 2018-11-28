#include <bits/stdc++.h>
using namespace std;

int t, T, n, d[10], s, k, x;
int main() {
    scanf("%d", &T);
    while(t++ < T) {
        memset(d, 0, sizeof d);

        scanf("%d", &n);

        if (n == 0) {printf("Case #%d: INSOMNIA\n", t); continue;}

        for(k=n, s=0; s != 10; k+= n)
            for(int x = k; x; x /= 10)
                if (d[x%10] == 0) s++, d[x%10]++;

        printf("Case #%d: %d\n", t, k-n);
    }
    return 0;
}
