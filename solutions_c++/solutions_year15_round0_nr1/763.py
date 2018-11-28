#include <cstdio>
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,k=0,l,i,sum,add;
    char s[1005];
    scanf("%d",&t);
    while(t--){
        scanf("%d %s",&l,s);
        for(sum=add=0,i=0;i<=l;i++){
            if(add+sum<i) add+=(i-add-sum);
            sum+=s[i]-48;
        }
        printf("Case #%d: %d\n",++k,add);
    }
}
