#include<stdio.h>
#include<string.h>



int main(void){
    int i,j,xx=1,y,z,test,n,m;
    char shin[500];

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&test);
    while(xx<=test){
        scanf("%s",shin);
        m=strlen(shin);
        n=1;
        for(i=1;i<m;i++){
            if(shin[i]!=shin[n-1])    shin[n++]=shin[i];
        }

        y=n-1+((shin[n-1]!='-')?0:1);
        printf("Case #%d: %d\n",xx,y);
        xx++;
    }
    return 0;
}

