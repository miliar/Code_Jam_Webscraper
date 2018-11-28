#include<cstring>
#include<cstdio>
#include <algorithm>
using namespace std;

const int maxn = 10005;

int data[maxn];
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int n, m;
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; ++i)
            scanf("%d",data+i);
        sort(data, data+n);
        int i, j = 0, ans = 0;
        for ( i = n-1; i > j; --i)
        {
            if (data[i]+data[j] > m)
                ++ans;
            else
            {
                ++ans;
                ++j;
            }
        }
        if (i == j)
            ++ans;
        printf("Case #%d: %d\n",++cas,ans);
    }
}
