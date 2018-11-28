#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_output_large.txt","w",stdout);
    int T,N;
    int m[1001];
    scanf("%d",&T);
    for (int index=1;index<=T;index++)
    {
        scanf("%d",&N);
        int s1=0;
        int rate = 0;
        scanf("%d",&m[0]);
        for (int i=1;i<N;i++)
        {
            scanf("%d",&m[i]);
            if (m[i]<m[i-1])
            {
                s1+=m[i-1]-m[i];
                rate=max(rate,m[i-1]-m[i]);
            }
        }
        //printf("rate=%d\n",rate);
        int s2=0;
        for (int i=1;i<N;i++)
        {
            s2+=min(m[i-1],rate);
        }
        printf("Case #%d: %d %d\n",index,s1,s2);
    }
    return 0;
}
