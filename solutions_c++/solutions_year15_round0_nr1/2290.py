#include<stdio.h>
char str[1005];
int main(){
    int T,S,aud,res;
    int i,j;
    scanf("%d\n",&T);
    for(i=0;i<T;i++){
        aud=0;
        res=0;
        scanf("%d ",&S);
        gets(str);
        for(j=0;j<S+1;j++){
            if(j>aud){
                res+=(j-aud);
                aud+=(j-aud);
            }
            aud+=(str[j]-'0');
        }
        printf("Case #%d: %d\n",i+1,res);
    }
}
