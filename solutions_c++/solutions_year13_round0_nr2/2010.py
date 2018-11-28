#include <cstdio>

using namespace std;

int data[105][105];

int main(void)
{
    int t, n, m, i, j, k, tc=0;
    bool vcell, valid;
    for (scanf("%d", &t);t--;)
    {
        scanf("%d%d", &n, &m);
        for (i=0;i<n;i++)
            for (j=0;j<m;j++)
                scanf("%d", &data[i][j]);
        valid=1;
        for (i=0;valid && i<n;i++)
            for (j=0;valid && j<m;j++)
            {
                for (k=0,vcell=1;vcell && k<m;k++)
                    vcell&=(data[i][j]>=data[i][k]);
                if (!vcell)
                {
                   for (k=0,vcell=1;vcell && k<n;k++)
                       vcell&=(data[i][j]>=data[k][j]);
                   valid&=vcell;
                }
            }
        printf("Case #%d: %s\n", ++tc, (valid) ? ("YES") : ("NO"));
    }
    return 0;
}
