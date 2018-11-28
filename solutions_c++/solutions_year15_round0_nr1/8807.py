#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
    int t,c=0;
    scanf("%d",&t);
    while(t--){
        long long n,res=0,cur=0;
        char x[1005];
        scanf("%lld %s",&n,x);
        cur=x[0]-'0';
        for(int i=1;i<strlen(x);i++){
            if(x[i]=='0')continue;
            if(cur<i){
                res+=(i-cur);
                cur=i;
            }
            cur+=(x[i]-'0');
        }
        printf("Case #%d: %lld\n",++c,res);
    }


    return 0;
}
