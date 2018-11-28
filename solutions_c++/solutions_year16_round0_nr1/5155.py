#include<stdio.h>
long long n,i,x,test,j = 2,a[10];
void add(long long num){
    while(num > 0){
        a[num % 10] = 1;
        num /= 10;
    }
}
bool check(){
    for(int i = 0; i <= 9; i++){
        if(a[i] == 0) return false;
    }
    return true;
}
int main(){
    freopen("lol.txt","r",stdin);
    freopen("555.txt","w",stdout);
    scanf("%lld",&test);
    for(int z = 1; z <= test; z++){
        scanf("%lld",&n);
        j = 1;
        for(int i = 0; i < 10; i++) a[i] = 0;
        while(1){
            add(n * j);
            //printf("%lld ",j * n);
            if(n == 0){
                printf("Case #%d: INSOMNIA\n",z);
                break;
            }
            if(check()){
                printf("Case #%d: %lld\n",z,j * n);
                break;
            }
            j++;
        }
    }
}