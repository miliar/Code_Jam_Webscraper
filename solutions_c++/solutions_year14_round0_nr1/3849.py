#include <stdio.h>

int T,a1,a2;
int M1[4][4],M2[4][4];

main(){
    scanf("%d",&T);
    for(int i=0;i<T;++i){
        scanf("%d",&a1);
        for(int r=0;r<4;++r){
            for(int c=0;c<4;++c)
                scanf("%d",M1[r]+c);
        }
        scanf("%d",&a2);
        for(int r=0;r<4;++r){
            for(int c=0;c<4;++c)
                scanf("%d",M2[r]+c);
        }
        int x=-1;
        --a1;--a2;
        for(int c1=0;c1<4;++c1){
            for(int c2=0;c2<4;++c2){
               // printf("%d %d\n",M1[a1][c1],M2[a2][c2]);
                if(M1[a1][c1]==M2[a2][c2]){
                    if(x<0)
                        x=M1[a1][c1];
                    else
                        x=17;
                }
            }
        }
        printf("Case #%d: ",i+1);
        //printf("%d",x);
        if(x<0)
            printf("Volunteer cheated!\n");
        else if(x>16)
            printf("Bad magician!\n");
        else
            printf("%d\n",x);

    }
}
