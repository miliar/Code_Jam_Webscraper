#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
double da[1010];
double db[1010];
vector < pair <double,int> > vi;
int main()
{
    int nc;
    scanf("%d",&nc);
    for(int ic=1;ic<=nc;ic++)
    {
        int n;
        scanf("%d",&n);
        vi.clear();
        for(int i=0;i<n;i++)
            scanf("%lf",da+i);
        for(int i=0;i<n;i++)
            scanf("%lf",db+i);
        for(int i=0;i<n;i++)
        {
            vi.push_back( make_pair(da[i],0) );
            vi.push_back( make_pair(db[i],1) );
        }
        sort(da,da+n);
        sort(db,db+n);
        sort(vi.begin(),vi.end());
        int ans1=0,pa,pb,ans2=0;
        pa=pb=0;
        for(int i=0;i<n;i++)
        {
            if (da[pa]<db[pb])
                pa++;
            else
            {
                ans1++;
                pa++;
                pb++;
            }
        }
        int t0=0;
        for(int i=0;i<2*n;i++)
        {
            if(0==vi[i].second)
            {
                t0++;
            }
            else
            {
                if (t0==0);
                else
                {
                    t0--;
                    ans2++;
                }
            }
        }
        printf("Case #%d: %d %d\n",ic,ans1,n-ans2);
    }
    return 0;
}
