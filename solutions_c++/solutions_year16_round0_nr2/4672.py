#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int T,ans;
char s[200];
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1; cas<=T; cas++)
    {
        printf("Case #%d: ",cas);
         memset(s,0,sizeof(s));
        scanf("%s",&s);
        ans=0;

        s[strlen(s)]='+';
        for (int i=0;i<strlen(s)-1;i++){
            if (s[i]!=s[i+1]) ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
