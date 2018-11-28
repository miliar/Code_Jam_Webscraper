#include <iostream>
using namespace std;

int main(void) {
    int n;
    cin >> n;

    for(int case_n = 1; case_n <= n; ++case_n) {
        long long int r, t;
        cin >> r >> t;

        long long int ans = 0;
        for(long long int i = r; ; i += 2) {
            t -= ((i + 1) * (i + 1)) - (i * i);
            if(t >= 0) ++ans;
            else break;
        }

        cout << "Case #" << case_n << ": " << ans << endl;
    }

    return 0;
}
