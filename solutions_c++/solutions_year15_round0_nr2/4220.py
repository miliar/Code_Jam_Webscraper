#include<cstdio>
#include<algorithm>
using namespace std;


int use[1010];
int main()
{
    int ti;
    scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",use+i);
        }
        int ret = 50000;
        for(int w=1;w<=1000;w++)
        {
            int ans = 0;
            for(int i=0;i<n;i++)
            {
                ans += (use[i] - 1) / w;
            }
            ret = min(ret, ans + w);
        }
        printf("Case #%d: %d\n", ca, ret);
    }
}
