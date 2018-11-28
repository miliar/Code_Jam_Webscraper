#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    freopen("in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++)
    {
        int n;
        double a[10000], b[10000];
        scanf("%d",&n);
        for(int i=0; i<n;i++)
        {
            scanf("%lf", &a[i]);
        }
        for(int i=0; i<n;i++)
        {
            scanf("%lf", &b[i]);
        }
        sort(a, a+n);

        sort(b, b+n);
        /*
        for(int i=0; i<n;i++)
        {
            printf("%lf %lf\n", a[i], b[i]);
        }
        */
        int score1 = 0, score2 = 0;
        for(int i=n-1, j=n-1; i>=0 && j>=0; j--)
        {
            if(a[i] > b[j])
            {
                i--;
                score1 ++;
            }
        }
        for(int i=0, j=0; i<n && j < n;j++)
        {
            if(a[i] < b[j])
            {
                i++;
                score2 ++;
            }
        }
        score2 = n - score2;
        printf("Case #%d: %d %d\n", cas, score1, score2);
    }
    return 0;
}
