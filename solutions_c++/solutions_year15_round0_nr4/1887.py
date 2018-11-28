#include<set>
#include<stdio.h>
#include<string.h>

int main() {
    int T,x,r,c;
    char bye;
    scanf("%d",&T);
    char ans[10];
    for(int t=0;t<T;t++){
        scanf("%d %d %d",&x,&r,&c);
        if(x==1) strcpy(ans,"GABRIEL");
        else if(x==2){
            if(r%2==0 || c%2==0) strcpy(ans,"GABRIEL");
            else strcpy(ans,"RICHARD");
        }
        else if(x==3){
            if((r==3 && c==2)||(r==3 && c==3)||(r==3 & c==4)||(c==3 && r==2)|| (c==3 & r==4)) strcpy(ans,"GABRIEL");
            else strcpy(ans,"RICHARD");
        }
        else{
            if((r==3 & c==4)||(c==4 && r==4)|| (c==3 & r==4)) strcpy(ans,"GABRIEL");
            else strcpy(ans,"RICHARD");
        }
        printf("Case #%d: %s\n",t+1,ans);
    }
    return 0;
}



