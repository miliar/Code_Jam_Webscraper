#include<stdio.h>
int n,i,x,t,smax=0,index[1010],count = 0,ans = 0;
char a[1010];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int z = 0; z < t; z++){
        count = 0,ans = 0;
        for(i = 0; i <= smax; i++) index[i] = 0;
        scanf("%d%s",&smax,a);
        for(i = 0; a[i]; i++)
            index[i] = a[i] - '0';
        for(i = 0; i <= smax; i++){
            if(index[i] > 0){
                if(count >= i)
                    count += index[i];
                else{
                    ans += i - count;
                    count += index[i] + i - count;
                }
            }
        }
        printf("Case #%d: %d\n",z + 1,ans);
    }
}
