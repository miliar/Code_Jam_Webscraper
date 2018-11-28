#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

int main()
{
    //freopen("test.txt", "r", stdin);
    //freopen("result.txt", "w", stdout);

    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    cout.precision(17);
    cout.setf( std::ios::fixed, std:: ios::floatfield );

    for (int Case = 1; Case <= T; Case++) {
        double C, F, X;
        cin >> C >> F >> X;

        double tmp = 0;
        double ans = X/2;

        for (int n = 1; n < 100001; n++) {
            tmp += C/(2.0 + double(n-1)*F);

            ans = min(ans, tmp + X / (2.0 + n*F) );
        }

        cout << "Case #" << Case << ": " << ans << "\n";
    }
}
