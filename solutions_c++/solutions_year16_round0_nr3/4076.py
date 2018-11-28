#include <cstdio>
#include <cmath>
int t,n,j,ct;
int b[35];
long long v[35];
long long prime(long long x)
{
    if(x%2==0) return 2;
    long long v=sqrt(x)+1;
    for(long long i=3;i<=v;i+=2)
    {
        if(((x/i)*i)==x) return i;
    }
    return -1;
}
void afis()
{
    for(int i=2;i<=10;i++)
    {
        long long nr=1,tot=0;
        for(int j=n;j>=1;j--)
        {
            if(b[j]==1) tot+=nr;
            nr*=i;
        }
        v[i]=prime(tot);
        if(v[i]==-1) return;
    }
    for(int i=1;i<=n;i++) printf("%d",b[i]);
    for(int i=2;i<=10;i++) printf(" %lld",v[i]);
    printf("\n");
    if(++ct==j) return;
   // for(int i=2;i<=10;i++) printf(" %d",i);
   // printf("\n");
}
void backtrack(int pos)
{
    if(pos==n) afis();
    else
    {
        for(int i=1;i>=0;i--)
        {
            b[pos]=i;
            backtrack(pos+1);
            if(ct==j) break;
        }
    }
}
int main()
{
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d%d",&n,&j);
        ct=0;
        b[1]=1;
        b[n]=1;
        printf("Case #%d:\n",i);
        backtrack(2);
    }
}
