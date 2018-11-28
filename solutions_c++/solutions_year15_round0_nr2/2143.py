#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int pancakes[1005];

int check(int mid, int n)
{
        for (int i = 1; i <= mid; i++)
        {
                int res = mid - i;
                int cnt = 0;
                for (int j = 0; j < n; j++)
                {
                        cnt += pancakes[j] / i + ((pancakes[j] % i) > 0) - 1;
                }
                if (cnt <= res) return 1;
        }
        return 0;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
            int n;
            cin >> n;
            for (int i = 0; i < n; i++) cin >> pancakes[i];

            int low = 1, high = 1000, mid;
            while (low < high)
            {
                    mid = (low + high) / 2;
                    if (check(mid, n)) high = mid;
                    else low = mid + 1;
            }

            printf("Case #%d: %d\n", cas, low);
    }

    return 0;
}
