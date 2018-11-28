#include<stdio.h>
#include<string.h>

char arr[1000];

int main(void){
    int i,j,T,n,tot,p;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1;i<=T;i++){
        scanf("%s",arr);
        n=strlen(arr);
        tot=1;
        for(j=0;j<n;j++){
            if(j==0){
                if(arr[j]=='+')p=1;
                else p=0;
            }
            else{
                if(p==1 && arr[j]=='-'){
                    p=0;
                    tot++;
                }
                else if(p==0 && arr[j]=='+'){
                    p=1;
                    tot++;
                }
            }
        }
        if(p==1)printf("Case #%d: %d\n",i,tot-1);
        else printf("Case #%d: %d\n",i,tot);
    }
}
