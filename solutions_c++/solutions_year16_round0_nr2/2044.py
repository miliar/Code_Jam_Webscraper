#include<bits/stdc++.h>
using namespace std;
int T,n;
char s[123456];
int main(){
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    scanf("%d",&T);
    for(int ti=1;ti<=T;ti++){
        printf("Case #%d: ",ti);
        scanf("%s",s);
        int n=strlen(s);
        int i=0,ans=0;
        char c=s[0];
        while(i+1<n){
            if(c!=s[i+1]){
                ans++;
                c=s[i+1];

            }
            i++;
        }
        if(c=='-') ans++;
        printf("%d\n",ans);
    }
}
