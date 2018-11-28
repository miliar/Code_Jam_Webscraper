#include<stdio.h>
#include<cstdlib>
#include<cstring>

using namespace std;

char sw(char x){
    return x=='-'?'+':'-';
}

int main(void){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d",&t);
    getchar();
    char cad[5000];
    for(int c = 1; c<=t; c++){
        scanf("%s",&cad);
        int k;
        scanf("%d",&k);
        getchar();
        //printf("--%s-%d--\n",cad,k);
        int n = strlen(cad);
        bool ok = true;
        int tot = 0;
        for(int i=0;i<n;++i){
            if(cad[i]=='-'){
                if(i>=n-k+1){
                    ok = false;
                    break;
                }else{
                    for(int j=0;j<k;++j){
                        cad[i+j]=sw(cad[i+j]);
                    }
                    tot++;
                }
            }
        }
        if(ok)
            printf("Case #%d: %d\n",c,tot);
        else
            printf("Case #%d: IMPOSSIBLE\n",c);
        }
    return 0;
}
