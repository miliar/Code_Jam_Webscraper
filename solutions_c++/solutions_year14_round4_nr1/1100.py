#include <bits/stdc++.h>

#define pb push_back

using namespace std;

const int nm=10002;

int n,a[nm];int m;
bool fr[nm];
vector<int> lastFree;

int dem()
{
    int i,kq=0;
    for(i=1;i<=n;++i)
    {
        kq++;
        if (a[i]+a[i+1]<=m) i++;
    }
    return kq;
}

int main()
{
    //freopen("a-small-attempt0.in","r",stdin);
    freopen("a-large.in","r",stdin);
    freopen("vd2.out","w",stdout);
    int t,i,kq,j;
    scanf("%d",&t);
    for(int it=1;it<=t;++it)
    {
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;++i) scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        kq=0;lastFree.clear();
        memset(fr,1,sizeof(fr));
        j=0;
        for(i=n;i>=1;--i)
        {
            if (fr[i])
            {
                if (i<=j) break;
                if (a[j]+a[i]>m)
                {
                    while (j>0 && (!fr[j] || a[j]+a[i]>m)) j--;
                }
                else
                {
                    while (j+1<i && a[j+1]+a[i]<=m) j++;
                }
                kq++;fr[i]=0;fr[j]=0;
                while (j<=n && !fr[j]) j++;
            }
        }
        j=0;
        for(i=1;i<=n;++i) if (fr[i]) j++;
        printf("Case #%d: %d\n",it,kq+j/2+j%2);
    }
}
