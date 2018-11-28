#include <iostream>
#include <string>
using namespace std;
int T;
int N;
char a[1234];
int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N;
        cin >> a;
        int ans = 0;
        int cur = 0;
        for(int i = 0; i <= N; i++) {
            if(a[i] != '0' && cur < i) {
                ans += i-cur;
                cur = i;
            }
            cur += static_cast<int>(a[i]-'0');
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
