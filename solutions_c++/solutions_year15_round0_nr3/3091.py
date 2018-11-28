#include"stdio.h"
#include"stdlib.h"

#define I 2
#define J 3
#define K 4

int sign(int n){
    return (n<0)?-1:1;
}

int abs(int n){
    return n*sign(n);
}

int main(){
    int  matrix[4][4] = { 
        {1,I,J,K}, 
        {I,-1,K,-J},
        {J,-K,-1,I}, 
        {K,J,-I,-1}
    };    
    /*
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)
            printf("%d,", matrix[i][j]);
        printf("\n");
    }
    */

    int t,l,x;
    char str[100000];
    scanf("%d", &t);
    for(int i=0;i<t;i++){
        scanf("%d%d%s", &l, &x, str);
        if(l*x<3){
            printf("Case #%d: NO\n", i+1);
            continue;
        }
        int finding = I;
        int running = 1;
        int curr;
        for(int a=0;a<x;a++){
            for(int b=0;b<l;b++){
                if(str[b] == 'i') curr = I;
                else if(str[b] == 'j') curr = J;
                    else curr = K;
//                printf("curr=%d\n", curr);            
                running = sign(running)*matrix[abs(running)-1][curr-1];
                if(finding != K && running == finding){
                    finding++;
                    running = 1;
                }
            }
        }
        if(finding == K && running == K)
            printf("Case #%d: YES\n", i+1);
        else
            printf("Case #%d: NO\n", i+1);
    }
}
