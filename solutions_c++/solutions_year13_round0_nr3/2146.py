#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
using namespace std;

bool ar[1001];

bool isPal(int x) {
    ostringstream os;
    os << x;
    string s = os.str();
    for (int i = 0; i < s.length() / 2; ++i) {
        if (s[i] != s[s.length() - 1 - i]) {
            return false;
        }
    }
    return true;
}

int main()
{
    for (int i = 0; i*i <= 1000; ++i) {
        ar[i*i] = isPal(i) & isPal(i*i);
    }
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        int a, b;
        cin >> a >> b;
        int ans = 0;
        for (int j = a; j <= b; ++j) {
            ans += ar[j];
        }
        cout << ans << "\n";
    }
}
