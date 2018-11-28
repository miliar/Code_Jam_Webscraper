#include <iostream>
#include <cstdio>
using namespace std;
int main()
{   int t;

    freopen("output.txt", "w", stdout);
    cin >> t;
    int a[1001];
    for (int kase = 1; kase <= t; kase++)
    {   int n;
        cin >> n;
        int m;
        for (int i = 0; i < n; i++)
        {   cin >> a[i];
            if (i == 0) m = a[i];
            m = max(m, a[i]);
        }
        int ans = 1000;

        for (int i = 1; i <= m; i++)
        {   int tmp = i;
            for (int j = 0; j < n; j++)
            {   if (a[j] > i)
                    tmp += (a[j] - i)%i == 0 ? (a[j] - i)/i: (a[j]-i)/i + 1;
            }
            ans = min(tmp, ans);
        }
        cout << "Case #" << kase <<": " << ans << endl;
    }
    fclose(stdout);

    return 0;
}
