#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
unsigned int T,N,J;

bool checkNum(uint64_t n){
    //printf("%u\n", n);
    if((n & 0x01) != 1)
        return false;
    if(((n>>(N-1)) & 0x01)  != 1)
        return false;
    return true;
}
uint64_t baseTo(uint64_t nn, int base){
    if(base == 2) return nn;
    uint64_t res = 0;
    uint64_t i = 1;
    uint64_t n = nn;
    while(n > 0){
        if((n & 0x1) == 1)
            res += i ;
        n =n >> 1;
        i *= base;
    }
    //printf("res : %d-> %d\n", nn,res);
    return res;
}
int isPrimer(uint64_t n){
    if(n == 1|| n ==2) return 1;
    int sqrtn = sqrt(n);
    //printf("%u\n", n);
    for(int i = 2; i <=sqrtn; i++){
        if(n % i == 0)
            return i;
    }
    return 1;
}
void printBin(uint64_t n){
    for(int i = N - 1; i >= 0 ; i--){
        char c = (n & (0x01 << i)) ? '1':'0';
        printf("%c", c);
    }
    printf(" ");
}
int fac[11];
int main(){

    scanf("%d\n%d\n%d", &T, &N, &J);
    printf("Case #1:\n");
    uint64_t start_num = 0x01 | (0x01 << (N - 1));
    uint64_t max = 0;
    for(int i = 0; i < N; i++)
        max = max | (0x1 << i);

    while(J){
        //printf("%u\n", start_num);
        int flag = true;
        for(int i = 2; i < 11; i ++){
            fac[i] = isPrimer(baseTo(start_num, i));
            if(fac[i] == 1){
                flag = false;
                break;
            }
        }
        if(flag){
            printBin(start_num);
            for(int i = 2; i < 10; i++)
                printf("%d ", fac[i]);
            printf("%d\n", fac[10]);
            J--;
        }
        start_num += 1;
        while(!checkNum(start_num)) start_num +=1;
        if(start_num >max ) break;
    }
    return 0;
}
