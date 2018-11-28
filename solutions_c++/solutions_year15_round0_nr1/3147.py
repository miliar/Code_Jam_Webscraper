#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i ++) {
        string s;
        int smax;
        cin >> smax >> s;
        int sum = 0;
        int res = 0;
        for(int needed = 0; needed <= smax; needed ++) {
            if(sum < needed) {
                res += needed - sum;
                sum = needed;
            }
            sum += s[needed] - '0';
        }
        cout << "Case #" << i + 1 << ": " << res << endl;
    }

    return 0;
}
