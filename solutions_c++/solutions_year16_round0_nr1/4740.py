#include <cstdio>
#include <cstring>

int T;
int digs[10];

bool checkDigs(){
    for(int i= 0; i < 10; i++)
        if(digs[i] == 0)
            return false;
    return true;
}

int countDigs(int n){
    int added = 0;
    while (n > 0) {
        int tmp = n % 10;
        if(digs[tmp] == 0)
            added++;
        digs[tmp]++;
        n = n / 10;
    }
    return added;
}
#define MAX_TRY 10000
int main(){
    int N;
    scanf("%d\n", &T);
    //printf("%d\n", T);
    for(int ca = 0; ca < T; ca++){
        scanf("%d\n", &N);
        //printf("%d\n", N);
        memset(digs, 0, sizeof(digs));
        countDigs(N);
        int added = 0;
        int add_time = 0;
        int INSOMNIA = false;
        int tot_time = 2;
        int now_n = N;
        while(!checkDigs()){
            now_n = N * tot_time;
            tot_time++;
            //printf("%d\n", now_n);
            added += countDigs(now_n);
            add_time++;
            if(add_time  > MAX_TRY ){
                if(added == 0){
                    INSOMNIA = true;
                    break;
                }else{
                    add_time = 0;
                    added = 0;
                }
            }
        }
        if(INSOMNIA)
            printf("Case #%d: INSOMNIA\n", ca+1);
        else
            printf("Case #%d: %d\n", ca+1, now_n);
    }
    return 0;
}
