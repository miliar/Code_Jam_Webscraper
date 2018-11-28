#include <stdio.h>

int main(){
    int a,jawab,jawab2,arr[5][5],arr2[5][5];
    freopen("A-small-attempt1.in","r",stdin);
    
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&a);
    for(int i = 0; i < a;i++){
        scanf("%d",&jawab);
        for(int i = 0; i < 4;i++){
            for(int j = 0; j < 4;j++){
                scanf("%d",&arr[i][j]);
            }
        }
        scanf("%d",&jawab2);
        for(int i = 0; i < 4;i++){
            for(int j = 0; j < 4;j++){
                scanf("%d",&arr2[i][j]);
            }
        }
        int ans = 0;
        int val;
        for(int i = 0; i < 4;i++){
            for(int j = 0; j < 4;j++){
                if(arr[jawab-1][i] == arr2[jawab2-1][j]){
                     ans++;
                    val = arr[jawab-1][i];
                } 
            }
        }
        printf("Case #%d: ",i+1);
        if(ans == 0) printf("Volunteer cheated!\n");
        else if(ans == 1)  printf("%d\n",val);
        else printf("Bad magician!\n");
    }
    return 0;
}
