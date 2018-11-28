#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("A-large.in","r",stdin);
    freopen("pA.txt","w",stdout);
    int T,p=1;
    scanf("%d",&T);
    while(T--){
        char str[10000];
        int i,ans=0,n,cnt;
        scanf("%d %s",&n,str);
        cnt=str[0]-'0';
        for(i=1;i<=n;i++){
            int num=str[i]-'0';
            if(cnt>=i)cnt+=num;
            else ans+=i-cnt,cnt=i+num;
        }
        printf("Case #%d: %d\n",p++,ans);
    }
    return 0;
}
