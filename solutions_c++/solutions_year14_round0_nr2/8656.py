#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

const int maxN = 4;

int main() {

    //freopen("inputB.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    int T;
    cin >> T;

    for (int caseNumber = 1; T; --T, ++caseNumber) {

        long double c, f, x, ans = 0;

        cin >> c >> f >> x;

        for (int k = 0; ; ++k) {
            long double currentTime = x / (k * f + 2.0), speed = 2.0;
            for (int i = 0; i < k; ++i) {
                currentTime += c / speed;
                speed += f;
            }

            if (currentTime < ans || ans == 0) {
                ans = currentTime;
            }
            else if (currentTime > ans)
                break;
        }

        cout << "Case #" << caseNumber << ": " << fixed << setprecision(8) << ans << endl;

    }

    return 0;

}
