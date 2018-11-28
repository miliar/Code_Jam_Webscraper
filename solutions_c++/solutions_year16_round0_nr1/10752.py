#include<stdio.h>
typedef long long int ll;
int ftab[10], total;

void nosplit(ll temp){
    while(temp > 0){
        int n = temp % 10;
        if (ftab[n] == 0)
            total--;
        ftab[n]++;
        temp /= 10;
    }
}

ll value(ll a){
    for (int i = 0; i < 10; i++)
        ftab[i] = 0;
    total = 10;
    int i = 1;
    while(1){
        nosplit(a*i);
        if (total == 0) return a*i;
        i++;
    }
}

int main(){
    int  T, i = 1;
    ll N;
    scanf("%d", &T);
    while(T--){
        scanf("%lld", &N);
        if(N == 0)
            printf("Case #%d: INSOMNIA\n", i);
        else
            printf("Case #%d: %lld\n", i,value(N));
        i++;
    }
    return 0;
}
