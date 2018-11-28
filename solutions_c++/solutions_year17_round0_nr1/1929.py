#include <stdio.h>
#include <string.h>



char p[1010];

int main() {
    int t, n;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        int cnt, k;
        scanf("%s %d", p, &k);
        n = strlen(p);
        cnt = 0;
        for (int i=0; p[i+k-1]; i++) 
            if (p[i]=='-') {
                for (int j=0; j<k; j++) 
                    p[i+j] = (p[i+j]=='+' ? '-' : '+');
                cnt++;
            }
        for (int i=n-1; i>=n-k; i--)
            if (p[i]=='-')
                cnt = -1;
        if (cnt>=0)
            printf("Case #%d: %d\n", o, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", o);
    }
}
