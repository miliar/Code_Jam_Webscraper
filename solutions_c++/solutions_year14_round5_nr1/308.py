#include<iostream>
#include<cstdio>
using namespace std;

int n,p,q,r,s;
long long trans[1000010], sum[ 1000010 ];

int main()
{
    int tt;
    cin >> tt;
    for (int ii = 0; ii < tt; ii++)
    {
        cin >> n >> p >> q >> r >> s;
        double ans = 0;
        for (int i = 1; i <= n; i++)
            trans[i] = ((i - 1) * p + q) % r + s;
        sum[1] = trans[1];
        for (int i = 2; i <= n; i++)
            sum[i] = sum[ i - 1 ] + trans[i];
        for (int i = 1; i <= n; i++)
        {
            int a = i, l = i, r = n;
            long long first = sum[i - 1],second = sum[i] - sum[i - 1],third = sum[ n ] - sum[i];
            long long minmax = -1;
            if (first >= second + third)
            {
                ans = max(ans,1.0 * (sum[ n ] - first) / sum[ n ]);
                break;
            }
            while (l + 3 < r)
            {
                int mid = (l + r) >> 1;
                second = sum[mid] - sum[i - 1];
                third = sum[ n ] - sum[ mid ];
                if (second > first && second > third)
                    r = mid;
                if (third > first && third > second)
                    l = mid;
                if (first > second && first > third)
                    break;
            }
            for (int j = l; j <= r; j++)
            {
                second = sum[j] - sum[ i - 1 ];
                third = sum[ n ] - sum[j];
                if (minmax == -1) minmax = max(max(second,third),first);
                minmax = min(minmax,max(max(second,third),first));
            }
            ans = max(ans,1 - 1.0 * minmax / sum[ n ]);
        }
        /*small
        for (int i = 0; i < n; i ++)
            for (int j = i; j < n; j++)
            {
                int a = i, b = j;
                double t1 = 2, t2 = 2,t3 = 2;
                if (a > 0)
                {
                    int s = sum[a - 1],ar= sum[n - 1] - s; 
                    t1 = ar * 1.0 / sum[n - 1];
                }
                if (b < n - 1)
                {
                    int ar = sum[b], s = sum[n - 1] - a;
                    t2 = ar * 1.0 / sum[n - 1];
                }
                int s = sum[b] - (a == 0 ? 0 : sum[a - 1]),ar = sum[n - 1] - s;
                t3 = ar * 1.0 / sum[n - 1];
                ans = max(min(min(t1,t2),t3),ans);
            }
        */
        printf("Case #%d: %.10f\n",ii + 1, ans);
    }
    return 0;
}
