#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

double p[201], f[202];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int N, K;
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; i++)
            scanf("%lf", &p[i]);
        sort(p, p + N);
        double ans = 0.0;
        for (int i = 0; i <= K; i++)
        {
//        for (int i = 0; i < (1 << N); i++)
//        {
//            int j = i, num = 0;
//            while (j)
//            {
//                num += 1;
//                j -= (j & (-j));
//            }
//            if (num != K) continue;
            vector<double> arr;
//            for (int j = 0; j < N; j++)
//                if ((i >> j) & 1) arr.push_back(p[j]);
            for (int j = 0; j < i; j++)
            {
                arr.push_back(p[j]);
            }
            for (int j = 0; j < K - i; j++)
            {
                arr.push_back(p[N - j - 1]);
            }
//            cout<<(int)arr.size()<<endl;
            for (int j = 0; j <= K; j++)
                f[j] = 0.0;
            f[0] = 1.0;
            for (int t = 0; t < K; t++)
            {
//                cout<<arr[t]<<" ";
                for (int j = K; j >= 0; j--)
                {
                    if (j > 0) f[j] = f[j - 1] * arr[t] + f[j] * (1.0 - arr[t]);
                    else       f[j] = f[j] * (1.0 - arr[t]);
//                    cout<<f[j]<<" "<<f[j + 1]<<endl;
                }
//                for (int j = 0; j <= K; j++)
//                    cout<<j<<" "<<f[j]<<endl;
            }
//            cout<<endl;
            ans = max(ans, f[K / 2]);
        }
        printf("Case #%d: %.8f\n", cas, ans);

    }
    return 0;
}
