#include<cstdio>
#include<iostream>

using namespace std;

int main(){
    int t;
    int r1;
    int map1[4][4];
    int r2;
    int map2[4][4];
    int i,j;
    int hasilIdx,hasilSama;
    
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("magic_output.txt","wt",stdout);
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++){
        hasilIdx = 0;
        hasilSama = 0;
        scanf("%d",&r1);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&map1[i][j]);
            }
        }
        r1--;
        scanf("%d",&r2);
        r2--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&map2[i][j]);
            }
        }
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(map1[r1][i]==map2[r2][j]){
                    hasilIdx=i;
                    hasilSama++;
                }
            }
        }
        if(hasilSama==0){
            printf("Case #%d: Volunteer cheated!\n",c);
        }else if(hasilSama>1){
            printf("Case #%d: Bad magician!\n",c);
        }else{
            printf("Case #%d: %d\n",c,map1[r1][hasilIdx]);
        }
    }
    while(getchar()!=EOF);
    return 0;
}
