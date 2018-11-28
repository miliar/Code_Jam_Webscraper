#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int T,cas,n,len,ans,now;
char s[1010];
int main(){
    cas=0;
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        ans=0;
        scanf("%d %s\n",&n,&s[0]);
        //printf("%d %d %s\n",cas,n,s);
        len=strlen(s);
        now=0;
        int t;
        for(int i=0;i<len;i++){
            t=0;
            //printf("%d %d\n",i,now);
            if(i>now) t=i-now,ans+=t;
            now+=s[i]-'0'+t;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
