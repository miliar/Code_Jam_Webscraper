#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int T;
int A[4][4], B[4][4], v[16];
int ra, rb;
int main(){
    scanf("%d", &T);
    for(int f=1;f<=T;f++){
        scanf("%d",&ra);
        ra--;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            scanf("%d", &A[i][j]);
            A[i][j]--;
        }
        memset(v,0,sizeof(v));
        for(int i=0;i<4;i++){
            v[ A[ra][i] ] = 1;
        }
        
        scanf("%d",&rb);
        rb--;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            scanf("%d", &B[i][j]);
            B[i][j]--;
        }
        int ans = -1, cnt = 0;
        for(int i=0;i<4;i++){
            if( v[ B[rb][i] ] == 1 ){
                ans = B[rb][i];
                cnt++;
            }
        }
        printf("Case #%d: ", f);
        if(cnt == 0){
            printf("Volunteer cheated!\n");
        }else if(cnt > 1){
            printf("Bad magician!\n");
        }else{
            printf("%d\n", ans+1);
        }
    }

    return 0;
}
