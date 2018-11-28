#include <stdio.h>

int u[16];

int main(){
    int tt,TT,x,a;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ){
        for( int i=0; i<16; i++ ){
            u[i] = 0;
        }
        for( int t=0; t<2; t++ ){
            scanf("%d",&a);
            a--;
            for( int i=0; i<4; i++ ){
                for( int j=0; j<4; j++ ){
                    scanf("%d",&x);
                    if(i==a){
                        u[x-1]++;
                    }
                }
            }
        }
        int f = 0;
        int d;
        for( int i=0; i<16; i++ ){
            if(u[i]==2){
                d = i;
                f++;
            }
        }
        if(f==1){
            printf("Case #%d: %d\n",tt+1,d+1);
        }else if(f==0){
            printf("Case #%d: Volunteer cheated!\n",tt+1);
        }else{
            printf("Case #%d: Bad magician!\n",tt+1);
        }
    }
}
