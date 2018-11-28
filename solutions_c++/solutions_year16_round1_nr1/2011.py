#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int cas = 1; cas <= t; cas++) {
        string str, ans;
        cin >> str;
        ans.insert(ans.begin(), str[0]);
        string a = ans, b = ans;
        for (int i = 1; i < str.size(); i++) {
            a.insert(a.begin(), str[i]);
            b.insert(b.end(), str[i]);
            ans = (a.compare(b) <= b.compare(a)) ? b : a;
            a = ans;
            b = ans;
        }
        cout << "Case #" << cas << ": " << ans << endl;
    }
    return 0;
}
