#include<stdio.h>
#include<stdlib.h>
char map[121][121];
int uP[121];
int dP[121];
int rP[121];
int lP[121];
int R,C;
int main(){
    int T;
    scanf("%d",&T);
    for(int ca = 0; ca < T ; ca++){
        scanf("%d %d",&R,&C);
        bool imposible = false;
        for(int i=0;i<121;i++)
            for(int j=0;j<121;j++)
                map[i][j] = 0;
        
        for(int i=0;i<121;i++)uP[i] = dP[i] = rP[i] = lP[i] = -1;
        for(int i=1;i<=R;i++){
            scanf("%s",map[i] + 1);
        }
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++){
                if(map[i][j] != '.'){
                    lP[i] = j;
                    break;
                }
            }
            for(int j=C;j>=1;j--){
                if(map[i][j] != '.'){
                    rP[i] = j;
                    break;
                }
            }
        }
        
        for(int j=1;j<=C;j++){
            for(int i=1;i<=R;i++){
                if(map[i][j] != '.'){
                    uP[j] = i;
                    break;
                }
            }
            for(int i=R;i>=1;i--){
                if(map[i][j] != '.'){
                    dP[j] = i;
                    break;
                }
            }
        }
        int ans = 0;
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++){
                if(map[i][j] == '.')continue;
                if(uP[j] == i && dP[j] == i && rP[i] == j && lP[i] == j){
                    imposible = true;
                }
                if(map[i][j] == '^'){
                    if(uP[j] == i)ans ++;
                }
                if(map[i][j] == '<'){
                    if(lP[i] == j)ans ++;
                }
                if(map[i][j] == '>'){
                    if(rP[i] == j)ans ++;
                }
                if(map[i][j] == 'v'){
                    if(dP[j] == i)ans ++;
                }
            }
        }
        printf("Case #%d: ", ca + 1);
        if(imposible){
            printf("IMPOSSIBLE\n");
        }else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
