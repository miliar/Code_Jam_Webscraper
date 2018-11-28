#include<stdio.h>
#include<stdlib.h>
int min(int a, int b){
    return (a > b) ? b : a;
}
int max(int a,int b){
    return (a > b) ? a : b;
}
int main(){
    int T;
    scanf("%d",&T);
    int x,r,c;
    for(int ca = 0; ca < T ;ca++){
        int tr,tc;
        scanf("%d %d %d",&x,&tr,&tc);
        r = max(tr,tc);
        c = min(tr,tc);
        bool G = true;
        if( (r * c) % x != 0){
            G = false;
        //    printf("2\n");
        }
        if((x + 1) / 2 > c){
            G = false;
        //    printf("3\n");
        }
        if(x > r){
            G = false;
        }
        if(x == 4 && r == 4 && c == 2){
            G = false;
        }
        if(G){
            printf("Case #%d: GABRIEL\n", ca + 1);
        }else{
            printf("Case #%d: RICHARD\n", ca + 1);
        }

    }
    return 0;
}
