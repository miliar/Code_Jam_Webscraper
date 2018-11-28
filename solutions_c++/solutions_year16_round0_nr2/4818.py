#include <cstdio>
#include <cstring>


int main(){
    int T;
    scanf("%d\n", &T);

    for(int ca = 1; ca <= T; ca++){
        char cakes[200];
        memset(cakes, 0, sizeof(cakes));
        scanf("%s\n", cakes);
        int res = 0;
        for(int i= 1; i < strlen(cakes); i++){
            if(cakes[i - 1] != cakes[i]){
                res ++;
            }
        }
        if(cakes[strlen(cakes) - 1] == '-')
            res++;
        printf("Case #%d: %d\n", ca, res);
    }


    return 0;
}
