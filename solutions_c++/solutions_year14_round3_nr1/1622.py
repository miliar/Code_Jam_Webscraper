#include<cstdio>
#include<cstdlib>

typedef long long int ll;

ll gcd(ll A, ll B){
    ll C = A%B;
    while(C != 0){
        A = B;
        B = C;
        C = A%B;
    }
    return B;
}

void solve(ll P, ll Q){
    if(P>Q || P==0){
        puts("impossible");
        return;
    }
    ll T = gcd(P, Q);
    P = P/T;
    Q = Q/T;
    int res = 0;
    while(res<41 && P<Q){
        if(Q%2){
            puts("impossible");
            return;
        }
        Q /= 2;
        res++;
    }
    if(res == 41){
        puts("impossible");
        return;
    }
    printf("%d\n", res);
    return;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        ll P, Q;
        scanf("%I64d/%I64d", &P, &Q);
        ll test = Q;
        int flag = 0;
        while(test > 1){
            if(test%2) flag = 1;
            test /= 2;
        }
        if(flag){
            puts("impossible");
            continue;
        }
        //printf("%I64d %I64d\n", P, Q);
        solve(P, Q);

        //printf("Case #%d: ", i);
        //solve1(P, Q);
    }
    return 0;
}
