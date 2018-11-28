#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
#define NAME "A-large"
#define UsingFile 1

int main(){
    if(UsingFile)freopen(NAME".in","r",stdin);
    if(UsingFile)freopen(NAME".out","w",stdout);
    int i,j,k,_T;
    scanf("%d",&_T);
    int CA=0;
    while(_T--){
        int x;
        char s[1115];
        scanf("%d%s",&x,s);
        int cnt[1115];
        for(i=0;i<=x;i++)cnt[i]=s[i]-'0';
        int ans=0;
        for(i=0;i<=x;i++){
            int tot=0;
            for(j=0;j<i;j++)tot+=cnt[j];
            if(tot<i)cmax(ans,i-tot);
        }
        printf("Case #%d: %d\n",++CA,ans);
    }
    return 0;
}

