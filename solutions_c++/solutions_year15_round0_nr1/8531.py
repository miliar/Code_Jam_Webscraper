#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    int n;
    string str;
    for (int i = 1; i <= T; i++) {
        cin >> n >> str;
        int ans = 0, cnt = 0;
        for (int j = 0; j < str.length(); j++) {
            ans = max(ans, j - cnt);
            cnt += str[j] - '0';
        }
        cout << "Case #" << i <<": " << ans << "\n";
    }
}
