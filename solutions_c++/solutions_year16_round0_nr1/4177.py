#include <cstdio>
#include <cstring>

bool hah[15];

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int totalCase, N, cases = 1;
    scanf("%d", &totalCase);
    while(totalCase--){
        memset(hah, 0, sizeof(hah));
        scanf("%d", &N);
        printf("Case #%d: ", cases++);
        if(N == 0){
            printf("INSOMNIA\n");
            continue;
        }
        for(int i = 1;; ++i){
            int tmp = i*N;
            while(tmp > 0){
                hah[tmp%10] = true;
                tmp/=10;
            }
            bool yes = true;
            for(int i = 0; i <= 9; ++i){
                if(!hah[i]){
                    yes = false;
                    break;
                }
            }
            if(yes){
                printf("%d\n", i*N);
                break;
            }
        }
    }
    return 0;
}
/*
5
0
1
2
11
1692
*/
