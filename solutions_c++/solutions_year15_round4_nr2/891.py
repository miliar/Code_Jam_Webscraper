#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);
    int T;
    cin >> T;
    cout.precision(100);
    for (int z = 0; z < T; ++z)
    {
        long double X, V;
        int N;
        long double ans;
        cin >> N >> V >> X;
        if (N == 1)
        {
            long double R, C;
            cin >> R >> C;
            if (C != X)
            {
                cout << "Case #" << z + 1 << ": " << "IMPOSSIBLE" << endl;
            }
            else
            {
                ans = V / R;
                cout << "Case #" << z + 1 << ": " << ans << endl;
            }
        }
        if (N == 2)
        {
            long double R1, C1, R2, C2;
            cin >> R1 >> C1 >> R2 >> C2;
            if (C1 > C2)
            {
                swap(C1, C2);
                swap(R1, R2);
            }
            if (X < C1 || X > C2)
            {
                cout << "Case #" << z + 1 << ": " << "IMPOSSIBLE" << endl;
            }
            else if (C1 == C2)
            {
                ans = V / (R1 + R2);
                cout << "Case #" << z + 1 << ": " << ans << endl;
            }
            else
            {
                long double V1, V2;
                V1 = (X * V - C2 * V) / (C1 - C2);
                V2 = V - V1;
                long double ans1, ans2;
                ans1 = V1 / R1;
                ans2 = V2 / R2;
                ans = max(ans1, ans2);
                cout << "Case #" << z + 1 << ": " << ans << endl;
            }
        }
    }
    return 0;
}
