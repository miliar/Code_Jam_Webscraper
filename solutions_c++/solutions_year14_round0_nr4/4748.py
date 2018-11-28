#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1010;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D_output_large.txt","w",stdout);
    int T,N;
    vector<int> v1, v2;
    int c1[MAXN],c2[MAXN];
    scanf("%d",&T);
    double d;
    for (int cases=1;cases<=T;cases++)
    {
        scanf("%d",&N);
        v1.clear();
        v2.clear();
        memset(c1,0,sizeof(c1));
        memset(c2,0,sizeof(c2));
        for (int i=0;i<N;i++)
        {
            scanf("%lf",&d);
            v1.push_back((int)(d*100000.0));
        }
        for (int i=0;i<N;i++)
        {
            scanf("%lf",&d);
            v2.push_back((int)(d*100000.0));
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        int war, detwar;
        war=detwar=0;
        for (int i=0;i<N;i++)
        {
            int p = upper_bound(v2.begin(),v2.end(),v1[i])-v2.begin();
            if (p>=N)
            {
                war++;
                c1[i]=N;
            }else{
                c2[p]++;
                c1[i]=p;
            }
        }
        c2[N]=0;
        int delta = 0;
        for (int i=N-1;i>=0;i--)
        {
            c2[i]+=c2[i+1];
            if (c2[i]>N-i) delta=max(delta,c2[i]-N+i);
        }
        war+=delta;
        for (int i=0;i<N;i++)
        {
            int counter = 0;
            for (int j=i;j<N;j++)
            {
                if (c1[j]>counter)
                {
                    counter++;
                }
            }
            detwar=max(detwar,counter);
        }
        printf("Case #%d: %d %d\n",cases,detwar,war);
    }
    return 0;
}
