#include <iostream>
using namespace std;

int caso() {
    int n, ans, partial;
    string st;
    cin >> n >> st;
    ans = partial = 0;
    
    for (int i = 0; i < int(st.size()); ++i) {
        if (st[i] == '0') continue;
        if (partial >= i)
            partial += st[i] - '0';
        else {
            ans += i - partial;
            partial += ans + st[i] - '0';
        }
    }
    
    return ans;
    
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
        cout << "Case #" << i + 1<< ": " << caso() << endl;
}