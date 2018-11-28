#include<stdio.h>
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int in=1;in<=T;in++){
        int l,exp=0,now=0,ans=0;
        char lev[1001];
        scanf("%d %s",&l,lev);
        while(now!=l){
             exp+=lev[now]-'0';
             if(exp>0){
                now++;
                exp--;
             }else{
                ans++;
                now++;
             }
        }
        printf("Case #%d: %d\n",in,ans);
            
    }
return 0;
}
