#include <stdio.h>
#include <math.h>

char jcode[100];
int next_alg;
int n;

void create_code(){
    jcode[0] = '1';
    for (int i=1; i<=n-2; i++)
        jcode[i] = '0';
    jcode[n-1] = '1';
    jcode[n] = '\0';

    next_alg = n-2;
}

void next_code(){
    jcode[next_alg] = '1';

    for (int i=next_alg+1; i<=n-2; i++)
        jcode[i] = '0';

    next_alg = n-2;
    while (jcode[next_alg] == '1')
        next_alg--;
}

long long code_to_base (int b){
    long long p = 1, ans = 0;

    for (int i=n-1; i>=0; i--){
        if (jcode[i] == '1')
            ans += p;
        p *= b;
    }

    return ans;
}

long long isNotPrime (long long x){
    if (x == 1) return false;
    if (x == 2) return true;

    for (int i=2; i<=sqrt(x)+1; i++)
        if (x%i == 0) return i;

    return 0;
}

int main(){
    int t, j;
    long long div[100];

    scanf ("%d %d %d", &t, &n, &j);
    printf ("Case #1:\n");

    create_code();

    while (j > 0){
        bool prime = false;

        for (int i=2; i<=10 && !prime; i++){
            div[i] = isNotPrime ( code_to_base(i) );
            if (div[i] == 0) prime = true;
        }

        if (!prime){
            j--;

            printf ("%s", jcode);
            for (int i=2; i<=10; i++)
                printf (" %lld", div[i]);
            printf ("\n");
        }

        if (j > 0)
            next_code();
    }

    return 0;
}
