#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc, x = 1;
    for(scanf("%d", &tc); tc--; ) {
        int n;
        scanf("%d", &n);

        printf("Case #%d: ", x++);
        if(!n) {
            printf("INSOMNIA\n");
            continue;
        }

        int c[12], uniq = 0;
        memset(c, 0, sizeof c);
        for(int i=1; i<100; i++) {
            int temp = n * i;
            while(temp) {
                c[temp % 10]++;
                if(c[temp % 10] == 1)
                    uniq++;
                if(uniq == 10) {
                    printf("%d\n", n * i);
                    goto lala;
                }
                temp /= 10;
            }
        }
        lala:;
    }

    return 0;
}