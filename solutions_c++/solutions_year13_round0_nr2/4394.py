#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,T;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        int n,m;
        scanf("%d %d",&n,&m);
        int grass[105][105];
        int i,j;
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                scanf("%d",&grass[i][j]);
        int cuti[105],cutj[105];
        for(i=0;i<n;i++)
        {
            cuti[i] = 0;
            for(j=0;j<m;j++)
                cuti[i] = max(cuti[i],grass[i][j]);
        }
        for(j=0;j<m;j++)
        {
            cutj[j] = 0;
            for(i=0;i<n;i++)
                cutj[j] = max(cutj[j],grass[i][j]);
        }
        bool poss=1;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(grass[i][j] != min(cuti[i],cutj[j])) poss=0;
            }
        }
        printf("Case #%d: ",t);
        if(poss) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
