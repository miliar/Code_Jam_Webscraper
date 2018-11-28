#include <iostream>
#include <cmath>

using namespace std;

int main() {

    long long r, t;

    int tc;
    cin >> tc;

    for(int tcn = 1; tcn <= tc; tcn++) {
        cout << "Case #" << tcn << ": ";

        cin >> r >> t;
        
        int ans = 0;

        while(t >= 0) {
            t -= (r+1)*(r+1) - r*r;
            r += 2;
            ans++;
        }

        cout << ans-1 << endl;
    }

    return 0;
}
