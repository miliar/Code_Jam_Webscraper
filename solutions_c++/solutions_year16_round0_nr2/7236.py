#include<stdio.h>

int main(){
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        char data[105]={0};
        int j,index,cnt=0; // index : 0(+) 1(-)
        scanf("%s",data);
        if(data[0]=='+')
            index = 0;
        else
            index = 1;
        for(j=1;data[j];j++){
            if(index==1 && data[j]=='+'){
                index=0;
                cnt++;
            }
            else if(index==0 && data[j]=='-'){
                index=1;
                cnt++;
            }
        }
        if(data[j-1]=='-')
            cnt++;
        printf("Case #%d: %d\n",i,cnt);
    }
    return 0;
}