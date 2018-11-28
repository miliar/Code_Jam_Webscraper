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

const int N=1e4+10;

int s[N],used[N];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,n,x;
    scf("%d",&T);
    forp(tcnt,0,T)
    {
        scf("%d%d",&n,&x);
        forp(i,0,n)scf("%d",s+i);
        sort(s,s+n);
        int ans=0;
        memset(used,0,sizeof(used));
        int p=0;
        form(i,n-1,-1)
        {
            if(used[i])continue;
            ans++;
            used[i]=1;
            if(p<i&&s[i]+s[p]<=x)
            {
                used[p]=1;
                p++;
            }
        }
        ptf("Case #%d: %d\n",tcnt+1,ans);
    }
    return 0;
}
