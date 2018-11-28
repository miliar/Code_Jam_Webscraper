#include <iostream>
#include <algorithm>

using namespace std;

int a[1<<14];

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        int n, m;
        cin >> n >> m;

        for (int i=0; i<n; i++)
            cin >> a[i];

        sort(a, a+n);

        int ans = 0;

        for (int i=0, j=n-1; i <= j; j--, ans++)
            i += a[i] + a[j] <= m;

        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
