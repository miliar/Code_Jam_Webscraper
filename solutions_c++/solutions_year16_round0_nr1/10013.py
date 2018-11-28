#include<stdio.h>

int mrc[10], cnt;

void mark(int i){
    if(!mrc[i]) mrc[i] = ++cnt;
}

int full(){
    return cnt == 10;
}

void clear(){
    for(int i = 0; i < 10; i++) mrc[i] = 0;
    cnt = 0;
}

void markThemAll(long long int num){
    int v;
    while(num > 0){
        v = num % 10;
        mark(v);
        num = num / 10;
    }
}

long long int multiple(int N){
    long long int r = 0;
    while(!full()){
        r+=N;
        markThemAll(r);
    }
    return r;
}

int main(void){
    int t, num;
    scanf("%d",&t);
    for (int i = 1; i <= t; i++){
        clear();
        scanf("%d",&num);
        printf("Case #%d: ",i);
        if(num > 0) printf("%lld\n",multiple(num));
        else printf("INSOMNIA\n");
    }
    return 0;
}
