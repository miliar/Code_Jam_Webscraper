#include<stdio.h>
#include<stdlib.h>

bool isPal(long long n)
{
    int i, j;
    int dig[50];
    for(i = 0; n > 0; i++) {
        dig[i] = n%10;
        n /= 10;
    }
    for(j = (i-1)/2; j >= 0; j--)
        if(dig[j] != dig[i-1-j]) return false;
    return true;
}

long long memo[100];

int main()
{
    //freopen("C-large-1.in", "r", stdin);
    //freopen("outC.txt", "w", stdout);
    int i, pos;
    int n = 0;
    char pal[50];
    long long j, k, aux, p = 1;
    for(i = 1, j = 1; i <= 6; i++) {
        p *= 10;
        // odd
        for(k = j; k < p; k++) {
            aux = k;
            pal[i-1] = aux%10 + '0';
            aux /= 10;
            for(pos = i-2; aux > 0; pos--) {
                pal[pos] = pal[2*i-2-pos] = aux%10 + '0';
                aux /= 10;
            }
            pal[2*i-1] = 0;
            aux = atoll(pal);
            if( isPal(aux*aux) ) {
                memo[n++] = aux*aux;
                //printf("%s   %I64d\n", pal, aux*aux);
            }
            /*
            for(pos = 0; pos < 2*i-1; pos++) printf("%c", pal[pos]);
            printf("\n");
            */
        }
        // even
        for(k = j; k < p; k++) {
            aux = k;
            for(pos = i-1; aux > 0; pos--) {
                pal[pos] = pal[2*i-1-pos] = aux%10 + '0';
                aux /= 10;
            }
            pal[2*i] = 0;
            aux = atoll(pal);
            if( isPal(aux*aux) ) {
                memo[n++] = aux*aux;
                //printf("%s   %I64d\n", pal, aux*aux);
            }
            /*
            for(pos = 0; pos < 2*i; pos++) printf("%c", pal[pos]);
            printf("\n");
            */
        }
        j = p;
    }

    //printf("n = %d\n\n", n);
    //printf("Range: 1 to %I64d%I64d\n", j-1, j-1);

    int t, x, y;
    long long a, b;

    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%I64d %I64d", &a, &b);
        for(i = 0; i < n && a > memo[i]; i++);
        for(pos = i; pos < n && memo[pos] <= b; pos++);
        printf("Case #%d: %d\n", x, pos-i);
    }
    return 0;
}
