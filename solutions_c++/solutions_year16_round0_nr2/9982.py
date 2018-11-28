#include <stdio.h>
#include <string.h>

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w+", stdout);
    int T, ok=1, nr=0, i, j, k;
    char S[101];
    scanf("%d", &T);
    for(k=1; k<=T; k++){
        scanf("%s", &S);
        for(i=strlen(S); i>=0; i--){
            if(S[i]=='-'){
                nr++;
                for(j=i; j>=0; j--)
                    if(S[j]=='-') S[j]='+';
                    else S[j]='-';
            }
        }
        printf("Case #%d: %d\n", k, nr);
        nr=0;
    }



}
