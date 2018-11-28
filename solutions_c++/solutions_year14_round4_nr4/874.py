#include <bits/stdc++.h>

#define pb push_back

using namespace std;

const int mm=1002;
const int nm=102;

int m,n;string a[mm];
int b[mm];int kq,dem;
set<string> x;

int f()
{
    int i,j,u,kq=0;string tg;

    for(i=1;i<=n;++i)
    {
        x.clear();
        for(j=1;j<=m;++j)
        {
            if (b[j]==i)
            {
                tg="";
                for(u=0;u<a[j].length();++u)
                {
                    tg+=a[j][u];
                    x.insert(tg);
                }
            }

        }
        if (x.size()) kq+=x.size()+1;
    }
    return kq;
}

void thu(int i)
{
    int j,tg;
    for(j=1;j<=n;++j)
    {
        b[i]=j;
        if (i==m)
        {
            tg=f();
            if (tg>kq)
            {
                kq=tg;dem=1;
            }
            else
                if (tg==kq) dem++;
        }
        else thu(i+1);
    }
}

int main()
{
    freopen("d-small-attempt0.in","r",stdin);
    freopen("vd.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(int it=1;it<=t;++it)
    {
        scanf("%d%d",&m,&n);
        for(i=1;i<=m;++i) cin>>a[i];
        kq=0;dem=0;
        thu(1);
        printf("Case #%d: %d %d\n",it,kq,dem);
    }
}
