#include<bits/stdc++.h>
using namespace std;
char s[1000+10];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,Case=0,n,ans,sum;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        scanf("%s",s);
        ans=sum=0;
        for(int i=0;i<=n;i++){
            if(sum<i){
                ans+=(i-sum);
                sum=i;
            }
            sum+=(s[i]-'0');
        }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
