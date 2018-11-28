#include <stdio.h>
#include <string.h>

int t,l;
int smax;
char s[1010];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++){
        scanf("%d%s",&smax,s);
        l = strlen(s);
        int ans=0,has=0;
        for(int i=0; i<l;i++){
            if(has<i){
                ans += i-has;
                has = i;
            }
            has += s[i]-'0';
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
