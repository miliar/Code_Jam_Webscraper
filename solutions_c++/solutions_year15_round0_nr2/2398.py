#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen ("B-large.in","r",stdin);
    //freopen ("output.txt", "w",stdout);
    int t;
    cin >> t;
    for (int q=0;q<t;q++)
    {
        int n;
        cin >> n;
        vector <int> a(n);
        for (int i=0;i<n;i++)
            cin >> a[i];

        int maxx=-1;
        for (int i=0;i<n;i++)
            maxx=max(maxx,a[i]);

        int ans=1;
        int count=1e8;
        for (int j = 1; j <= maxx; j++)
        {
            ans = j;
            for (int k = 0; k < n; k++)
            {
                if (a[k] > j)
                {
                    ans += (a[k] % j == 0 ? a[k] / j - 1 : a[k] / j);
                }
            }
            count = min(ans, count);
        }
        cout << "Case #" << q+1 << ": " << count << endl;
    }
    return 0;
}
