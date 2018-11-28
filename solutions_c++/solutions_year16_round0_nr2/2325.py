#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

#define MAXN 110
using namespace std;

typedef long long LL;
char s[MAXN];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,t,n,ans;
    for(scanf("%d",&t),i=1;i<=t;++i){
        scanf("%s",s); n=strlen(s);
        for(j=ans=0,k=1;k<=n;++k)
            if(s[k]!=s[j]) ++ans,j=k;
        if(s[n-1]=='+') --ans;
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
