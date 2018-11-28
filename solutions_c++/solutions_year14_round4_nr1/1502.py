#include <cstdio>
#include <algorithm>
using namespace std;

int n, c;
int list[10010];

int main()
{
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T; ++cas)
    {
        scanf("%d %d", &n, &c);
        for(int i=0; i<n; ++i)
            scanf("%d", &list[i]);
        sort(list, list+n);
        int ans = 0, p = 0;
        for(int i=n-1; i>=p; --i)
        {
            ++ans;
            if(list[i] + list[p] <= c)
                ++p;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
