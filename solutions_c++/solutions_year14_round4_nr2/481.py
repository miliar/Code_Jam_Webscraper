#include <cstdio>
#include <algorithm>

using namespace std;

int vals[1005];
int ord[1005];
int dp[1005][1005];
int pre[1005];
int posle[1005];

int tc;

int main()
{
    freopen("D:/in.txt","r",stdin);
    freopen("D:/out.txt","w",stdout);
    scanf("%d",&tc);
    for (int it=1; it<=tc; it++)
    {
        int n;
        scanf("%d",&n);
        for (int i=1; i<=n; i++)
        {
            scanf("%d",&vals[i]);
            ord[i]=vals[i];
        }
        sort(ord+1,ord+1+n);
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++)
                if (vals[i]==ord[j])
                {
                    vals[i]=j;
                    break;
                }
        int p=1;
        int k=n;
        int sol=0;
        for (int i=1; i<n; i++)
        {
            int pl;
            for (int j=p; j<=k; j++)
                if (vals[j]==i)
                    pl=j;
            if (k-pl<=pl-p)
            {
                sol+=k-pl;
                while (pl<k)
                {
                    swap(vals[pl],vals[pl+1]);
                    pl++;
                }
                k--;
            }
            else
            {
                sol+=pl-p;
                while (pl>p)
                {
                    swap(vals[pl],vals[pl-1]);
                    pl--;
                }
                p++;
            }
        }
        printf("Case #%d: %d\n",it,sol);


    }

}
