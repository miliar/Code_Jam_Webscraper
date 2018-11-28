#include<stdio.h>
int n,i,x,test,ans=0;
char a[110];
int main(){
    freopen("lol.txt","r",stdin);
    freopen("555.txt","w",stdout);
    scanf("%d",&test);
    for(int z = 1; z <= test; z++){
        for(i = 0; i < 105; i++) a[i] = 0;
        scanf("%s",a);
        ans = 0;
        
        for(i = 0; a[i]; i++){
            if(a[i] == '-'){
                x = i;
                while(a[x] == '-' && a[x + 1] == '-') x++;
                if(i == 0) ans++;
                else ans += 2;
                i = x;
            }
        }
        printf("Case #%d: %d\n",z,ans);
    }

}