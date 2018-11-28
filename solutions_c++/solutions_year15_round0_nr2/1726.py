#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        int n;
        int a[1024];
        cin >> n;

        for (int i=0; i<n; i++)
            cin >> a[i];

        int best = 1 << 30;

        for (int i=1; i<=1000; i++)
        {
            int cur = i;
            for (int j=0; j<n; j++)
                cur += (a[j] - 1) / i;
            best = min(cur, best);
        }

        cout << "Case #" << tt << ": " << best << endl;
    }

    return 0;
}
