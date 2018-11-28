#include <iostream>
#include <algorithm>

#define N 10010

using namespace std;

int a[N];

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        int n, x;
        cin >> n >> x;
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        sort(a, a + n);

        int i = 0, j = n - 1;
        int ans = 0;
        while (i <= j)
        {
            ++ans;
            if (a[i] + a[j] <= x)
            {
                ++i;
                --j;
            }
            else
                --j;
        }
        cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
}
