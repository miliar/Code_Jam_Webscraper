#include <iostream>

using namespace std;

pair<int, int> x[1024];

int a[2][1024];

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        int n;
        cin >> n;

        for (int i=0; i<n; i++)
        {
            cin >> x[i].first;
            x[i].second = i;
        }

        sort(x, x+n);

        int *cur = a[0];
        int *next = a[1];

        cur[0] = 0;

        for (int i=0; i<n; i++)
        {
            for (int j=0; j <= i + 1; j++)
                next[j] = n*n;

            int k = 0;
            for (int j=0; j<i; j++)
                k += x[j].second < x[i].second;

            next[0] = abs(n - 1 - i - x[i].second + k) + cur[0];
            next[i+1] = abs(x[i].second - k) + cur[i];

            for (int j=1; j<=i; j++)
                next[j] = min(abs(x[i].second - k) + cur[j-1], abs(n - i - 1 - x[i].second + k) + cur[j]);

//            for (int j=0; j<=i+1; j++)
//                cout << next[j] << " ";
//            cout << endl;

            swap(cur, next);
        }

        int ans = n*n;

        for (int i=0; i<n; i++)
            ans = min(ans, cur[i]);


        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
