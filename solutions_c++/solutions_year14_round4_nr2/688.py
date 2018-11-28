#include<bits/stdc++.h>
#define scf scanf
#define ptf printf
#define forp(i,j,k) for(int i=j;i<k;i++)
#define form(i,j,k) for(int i=j;i>k;i--)
#define sz(x) (int)x.size()
#define pb push_back
#define fst first
#define scd second
using namespace std;

typedef long long LL;

const int N=1010,oo=1e9+10;

int a[N];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,n;
    scf("%d",&T);
    forp(tcnt,0,T)
    {
        scf("%d",&n);
        forp(i,0,n)scf("%d",a+i);
        int ans=0,mn,mi,l,r;
        l=0;r=n-1;
        forp(i,0,n)
        {
            mn=oo;
            forp(j,l,r+1)
                if(a[j]<mn)
                {
                    mn=a[j];
                    mi=j;
                }
            ans+=min(mi-l,r-mi);
            if(mi-l<=r-mi)
            {
                form(j,mi,l)a[j]=a[j-1];
                l++;
            }
            else
            {
                forp(j,mi,r)a[j]=a[j+1];
                r--;
            }
        }
        ptf("Case #%d: %d\n",tcnt+1,ans);

    }
    return 0;
}
