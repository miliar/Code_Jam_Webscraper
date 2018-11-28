//
// Created by Acka on 4/9/16.
//

#define ROOT    33333333
#define PRIME_N 2050943

#include <stdio.h>

int p[PRIME_N] = { 2, };
int n[16] = {1,}, d[13], N, J, pcnt = 1, cnt;
bool notp[ROOT + 1] = {true, true, false, };

void set_prime(){
    for(int i = 4; i <= ROOT; i += 2) notp[i] = true;

    for(long long int i = 3, j; i <= ROOT; i += 2){
        if(notp[i]) continue;

        p[pcnt++] = i;
        for(j = i * i; j <= ROOT; j += 2 * i)
            notp[j] = true;
    }
}

void get_ans(int idx){
    if(J <= cnt) return ;

    if(N <= idx + 1){
        bool pri = false, div;

        for(long long int i = 2, x, j, k; i <= 10 && !pri; i++){
            for(x = 0, j = 0; j < N; j++){
                x *= i; x += n[j];
            }

            div = false;
            for(k = 0; k < pcnt; k++) {
                if(x < (long long)p[k] * p[k]) break;
                if (!(x % p[k])) {
                    d[i] = p[k];
                    div = true;
                }
            }

            if(!div) pri = true;
        }

        if(!pri){
            for(int i = 0; i < N; i++) printf("%d", n[i]);
            for(int i = 2; i <= 10; i++) printf(" %d", d[i]);
            printf("\n");
            cnt++;
        }
        return ;
    }

    n[idx] = 0; get_ans(idx + 1);
    n[idx] = 1; get_ans(idx + 1);
}

int main()
{
    set_prime();

    freopen("/Users/acka/ClionProjects/ProblemSolving/C-small-attempt0.in", "r", stdin);
    freopen("/Users/acka/ClionProjects/ProblemSolving/C-small-attempt0.out", "w", stdout);

    int tc, st = 1; for(scanf("%d", &tc); tc--;){
        scanf("%d %d", &N, &J);

        printf("Case #%d:\n", st++);
        n[N - 1] = 1;
        cnt = 0;
        get_ans(1);
    }
    return 0;
}
