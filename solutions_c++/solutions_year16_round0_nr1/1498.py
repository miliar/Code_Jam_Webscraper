#include <cstdio>

bool dig[10];

int main(){
    int T, tc = 0;
    scanf("%d", &T);
    
    while(T--){
        int N;
        scanf("%d", &N);
        
        if(N == 0){
            printf("Case #%d: INSOMNIA\n", ++tc);
            continue;
        }
        
        int num = 0, cnt = 0;
        for(int i=0; i<10; i++) dig[i] = false;
        
        while(cnt < 10){
            num += N;
            int tmp = num;
            
            while(tmp){
                if(!dig[tmp%10]) cnt++;
                dig[tmp%10] = true;
                tmp /= 10;
            }
        }
        
        printf("Case #%d: %d\n", ++tc, num);
    }
}
