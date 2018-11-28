#include <iostream>

#define N 1010

using namespace std;

int a[N];

int find_min(int *a, int l, int r)
{
    int minj = l;
    for (int i = l + 1; i <= r; ++i)
        if (a[i] < a[minj])
            minj = i;
    return minj;
}

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        int l = 0, r = n - 1;
        int ans = 0;
        while (l < r)
        {
            int j = find_min(a, l, r);
            if (j - l < r - j)
            {
                for (int i = j; i > l; --i)
                {
                    ++ans;
                    a[i] = a[i - 1];
                }
                ++l;
            }
            else
            {
                for (int i = j; i < r; ++i)
                {
                    ++ans;
                    a[i] = a[i + 1];
                }
                --r;
            }
        }
        cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
}
