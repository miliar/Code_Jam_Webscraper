#include <bits/stdc++.h>

#define pb push_back

using namespace std;

const int nm=1002;

int n,a[nm],b[nm];
int vt[nm];

bool kt()
{
    int i;
    for(i=1;i<n;++i) if (b[i]>b[i+1]) break;
    if (i>=n) return 1;
    for(i++;i<n;++i) if (b[i]<b[i+1]) return 0;
    return 1;
}

int f()
{
    int i,j;
    for(i=1;i<=n;++i)
    {
        for(j=1;j<=n;++j) if (b[i]==a[j]) break;
        vt[i]=j;
    }
    int kq=0;
    for(i=1;i<=n;++i)
    {
        for(j=1;j<i;++j) if (vt[j]>vt[i]) kq++;
    }
    return kq;
}

int main()
{
    freopen("b-small-attempt0.in","r",stdin);
    freopen("vd.out","w",stdout);
    int t,i,kq;
    scanf("%d",&t);
    for(int it=1;it<=t;++it)
    {
        scanf("%d",&n);
        for(i=1;i<=n;++i)
        {
            scanf("%d",&a[i]);b[i]=a[i];
        }
        sort(b+1,b+n+1);
        kq=n*n;
        do
        {
            if (kt()) kq=min(kq,f());
        }
        while (next_permutation(b+1,b+n+1));
        printf("Case #%d: %d\n",it,kq);
    }
}
