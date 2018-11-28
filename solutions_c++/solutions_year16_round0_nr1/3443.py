#include <stdio.h> 

void solve(int N) {
    int seen[10];
    for(int i=0; i<10; ++i) seen[i]=0;
    int cnt = 0;
    int num = N;
    int i;
    for (i=1; i<101, cnt != 10; ++i) {
        num = N*i;
        do {
            if (seen[num % 10] == 0) {
                cnt++;
                seen[num % 10] = 1;
            }
            num /= 10;
        } while (num > 0);
    }
    if(cnt != 10)
        printf("INSOMNIA");
    else 
        printf("%d",(i-1)*N);
}

int main(){
    int T; 
    int N;
    scanf("%d", &T);
    for(int i=0;i<T;++i) {
        scanf("%d", &N);    
        printf("Case #%d: ", i+1);
        if (N == 0) 
            printf("INSOMNIA");
        else solve(N);
        printf("\n");
    }
}
