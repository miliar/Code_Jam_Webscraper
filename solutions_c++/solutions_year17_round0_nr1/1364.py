#include <cstdio>
#include <cstring>
int t,k,n,cnt;
char s[1005];
void flip(int p) {
    ++cnt;
    for (int i=p;i<p+k;++i)
        s[i]=s[i]=='-'?'+':'-';
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        scanf("%s%d",s,&k);
        n=strlen(s);
        cnt=0;
        for (int i=0;i<=n-k;++i)
            if (s[i]=='-')
                flip(i);
        bool f=false;
        for (int i=n-k+1;i<n;++i)
            if (s[i]=='-')
                f=true;
        printf("Case #%d: ",cas);
        if (f)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",cnt);
    }
    return 0;
}
