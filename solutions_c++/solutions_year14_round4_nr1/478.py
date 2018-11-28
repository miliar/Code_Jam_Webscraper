#include <cstdio>
#include <algorithm>

using namespace std;

int vals[10005];
int n,tc;
int mx;

int main()
{
    freopen("D:/in.txt","r",stdin);
    freopen("D:/out.txt","w",stdout);
    scanf("%d",&tc);
    for (int it=1; it<=tc; it++)
    {
        scanf("%d%d",&n,&mx);
        for (int i=1; i<=n; i++)
            scanf("%d",&vals[i]);
        sort(vals+1,vals+1+n);
        int p,k;
        int sol=0;
        p=1;
        k=n;
        while (p<=k)
        {
            if (p==k)
            {
                sol++;
                k--;
                continue;
            }
            if (vals[p]+vals[k]<=mx)
            {
                p++;
                k--;
                sol++;
            }
            else
            {
                k--;
                sol++;
            }
        }
        printf("Case #%d: %d\n",it,sol);
    }
}
