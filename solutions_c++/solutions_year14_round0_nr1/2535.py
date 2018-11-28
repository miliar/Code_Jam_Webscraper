#include <stdio.h>
#include <stdlib.h>
int main(void){
    int T, t;
    scanf("%d", &t);
    for(T = 1; T <= t; T++){
        int ans1, ans2;
        int i, j, m[5][5], pos[17]={0};
        scanf("%d", &ans1);
        for(i = 1; i < 5; i++)
            for(j = 1; j < 5; j++)
                scanf("%d", &m[i][j]);
        i = ans1;
        for(j = 1; j < 5; j++)
            pos[m[i][j]]++;
        
        scanf("%d", &ans2);
        for(i = 1; i < 5; i++)
            for(j = 1; j < 5; j++)
                scanf("%d", &m[i][j]);
        i = ans2;
        for(j = 1; j < 5; j++)
            pos[m[i][j]]++;
        
        int cnt = 0, ans = 0;
        for(i = 1; i <= 16; i++){
            if(pos[i] == 2){
                cnt ++;
                ans = i;
            }
        }
        if(cnt > 1)
            printf("Case #%d: Bad magician!\n", T);
        else if(cnt == 1)
            printf("Case #%d: %d\n", T, ans);
        else if(cnt == 0)
            printf("Case #%d: Volunteer cheated!\n", T);
    }
    return 0;
}