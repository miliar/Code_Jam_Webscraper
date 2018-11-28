#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main(){
    int t, l1, l2, v1[7][7], v2[7][7];
    int vis[20];

    scanf("%d", &t);
    for(int nt = 1; nt <= t; ++nt){
        scanf("%d", &l1);
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                scanf("%d", &v1[i][j]);
        
        scanf("%d", &l2);
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                scanf("%d", &v2[i][j]);
        
        memset(vis, 0, sizeof(vis));
        for(int i = 1; i <= 4; ++i){
            vis[v1[l1][i]]++;
            vis[v2[l2][i]]++;
        }

        int cand = -1;
        for(int i = 1; i <= 16; ++i){
            if(vis[i] == 2){
                if(cand == -1)
                    cand = i;
                else{
                    cand = -2;
                    break;
                }
            }
        }
        if(cand == -1)
            printf("Case #%d: Volunteer cheated!\n", nt);
        else if(cand == -2)
            printf("Case #%d: Bad magician!\n", nt);
        else
            printf("Case #%d: %d\n", nt, cand);
    }

    return 0;
}
