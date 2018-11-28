#include<stdio.h>

int main(){
    int t,a,b,k,d,ans,s;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d%d%d",&a,&b,&s);
        ans=0;
        for(int j =0;j<a;j++){
            for(int k=0;k<b;k++){
                d=j&k;
                if(d<s)
                    ans++;
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
