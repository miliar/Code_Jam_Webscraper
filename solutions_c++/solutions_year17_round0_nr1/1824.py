#include <cstdio>
#include <cstring>

const int sz = 110;
char a[sz];

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for(int caseno=1;caseno<=cases;caseno++) {
        int k, len, count=0;
        scanf(" %s %d", a, &k);
        len = strlen(a);

        for(int i=0;i+k<=len;i++)if(a[i]=='-') {
            for(int j=0;j<k;j++) {
                a[i+j] = (a[i+j]=='-') ? '+' : '-';
            }
            ++count;
        }

        printf("Case #%d: ", caseno);
        for(int i=0;i<len;i++)if(a[i]=='-') {
            puts("IMPOSSIBLE");
            goto END;
        }
        printf("%d\n", count);
        END:;
    }
}
