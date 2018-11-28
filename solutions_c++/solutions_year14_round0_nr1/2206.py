#include<cstdio>
#include<cstdlib>

int main(void){
    int T;
    int pos[20];
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        for(int j = 0; j < 20; j++) pos[j] = 0;
        int tar, tmp;
        scanf("%d", &tar);
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++){
                scanf("%d", &tmp);
                if(j+1 == tar) pos[tmp] = 1;
            }
        scanf("%d", &tar);
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++){
                scanf("%d", &tmp);
                if(j+1 == tar) pos[tmp]++;
            }
        int ans = -1;
        for(int j = 1; j <= 16; j++){
            if(pos[j]==2 && ans==-1) ans = j;
            else if(pos[j]==2 && ans!=-1) ans = -2;
        }
        if(ans == -1) puts("Volunteer cheated!");
        else if(ans == -2) puts("Bad magician!");
        else printf("%d\n", ans);
    }
    return 0;
}
