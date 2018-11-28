#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#define N 1010
#define eps 1e-7
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
using namespace std;
bool cmp(double x,double y)
{
    return x>y;
}
double nao[N],ken[N];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large-out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas;
    for(cas=1;cas<=T;cas++)
    {
        int n,i,j,k;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&nao[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&ken[i]);
        sort(nao,nao+n,cmp);
        sort(ken,ken+n,cmp);
        int y,z;
        int ni,nj,ki,kj;
        ni=ki=0;nj=kj=n-1;
        y=z=0;
        for(i=0;i<n;i++)
        {
            if(nao[ni]>ken[ki])
            {
                y++;
                ni++;ki++;
            }
            else if(nao[ni]<ken[ki])
            {
                nj--;ki++;
            }
            else
            {
                if(nao[nj]>ken[kj])
                {
                    y++;
                    nj--;kj--;
                }
                else
                {
                    nj--;ki++;
                }
            }

        }
        ni=ki=0;nj=kj=0;
        for(i=0;i<n;i++)
        {
            if(ken[ni]>nao[ki])
            {
                z++;
                ni++;ki++;
            }
            else if(ken[ni]<nao[ki])
            {
                nj--;ki++;
            }
            else
            {
                if(ken[nj]>nao[kj])
                {
                    z++;
                    nj--;kj--;
                }
                else
                {
                    nj--;ki++;
                }
            }
        }
            printf("Case #%d: %d %d\n",cas,y,n-z);
        
    }
}
