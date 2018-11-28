#include<bits/stdc++.h>
using namespace std;

int t,len,ans,prv;
char s[222222];


int main(){
    freopen("bb.in","r",stdin);
    freopen("b.txt","w",stdout);
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++){
        printf("Case #%d: ",ca);
        scanf("%s",&s);
        len = strlen(s);
        ans = 0;
        prv=0;
        if(s[0]=='-')prv=1;
        for(int i = 1;i<len;i++){
            if(s[i]!=s[i-1]){
                ans++;
                prv=1-prv;
            }
        }
        if(prv)ans++;
        printf("%d\n",ans);

    }

    return 0;
}
