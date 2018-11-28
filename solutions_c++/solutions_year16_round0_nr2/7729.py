#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,N,j,k;
    int num;
    int check;
    int x;
    char s[100];
    int p[100];
    scanf("%d",&N);
    for(k=0;k<N;k++){
    check=0;
    for(i=0;i<100;i++){
        s[i]=NULL;
        p[i]=NULL;
    }
    scanf("%s",s);
    num=strlen(s);
    for(i=num-1;i>=0;i--){
            if(s[i]=='+'){
                p[i]=1;
            }
            if(s[i]=='-'){
                p[i]=0;
            }
    }
    for(i=strlen(s)-1;i>=0;i--){
        if(p[i]==0){
            for(x=i;x>=0;x--){
                if(p[x]==0){
                    p[x]=1;
                }
                else if(p[x]==1){
                    p[x]=0;
                }
            }
                check=check+1;
        }
    }
    printf("case #%d: %d\n",k+1,check);
    }
    return 0;
}
