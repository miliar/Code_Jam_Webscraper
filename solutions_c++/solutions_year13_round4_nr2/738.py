#include <iostream>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t;
    cin >> t;
    for (int task = 1; task <= t; task++) {
        long long n, p, guaranteed, could;
        cin >> n >> p;
        if (p <= (1LL << (n - 1))) {
            guaranteed = 0;
        } else {
            long long temp = p - 1;
            long long canloss = 1;
            while (temp) {
                if (temp & 1) {
                    canloss++;
                } else {
                    canloss = 1;
                }
                temp >>= 1;
            }
            guaranteed = (1LL << canloss) - 2;
            if (p == (1LL << n)) {
                guaranteed = (1LL << n) - 1;
            }
        }
        for (long long turn = 1; turn <= n + 1; turn++) {
            if (p < (1LL << turn)) {
                could = (1LL << n) - (1LL << (n - turn + 1));
                break;
            }
        }
        cout << "Case #" << task << ": " << guaranteed << " " << could << endl;
    }
    
    return 0;
}
