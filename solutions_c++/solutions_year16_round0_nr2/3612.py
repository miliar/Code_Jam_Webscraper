#include <cstdio>
#include <cstring>
#include <queue>
#define nmax 12
using namespace std;
int t,ok,v[1<<nmax];
char s[nmax];

int fliping(int p,int r)
{
    int i,k=0;
    for (i=r;i>=0;i--) {
        k<<=1;
        k^=((p&(1<<i))==0);
    }
    for (i=r+1;s[i];i++)
        k^=p&(1<<i);

    return k;
}
int main()
{
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    int i,j,k,r,p;
    scanf("%d",&t);
    for (i=1;i<=t;i++) {
        memset(v,0,sizeof(v));
        memset(s,0,sizeof(s));
        scanf("%s",&s);
        for (j=0;j<(1<<nmax);j++)
            v[j]=1<<30;
        for (j=0,k=0;s[j];j++)
            if (s[j]=='+')
                k+=1<<j;
        v[k]=0;
        for (j=0,ok=1;ok;j++) {
            ok=0;
            for (p=0;p<(1<<nmax);p++)
            if (v[p]==j)
                for (r=0,ok=1;s[r];r++) {
                    k=fliping(p,r);
                    v[k]=min(v[k],v[p]+1);
                }
        }
        for (j=0;s[j];j++);
        printf("Case #%d: %d\n",i,v[(1<<j)-1]);
    }
    return 0;
}
