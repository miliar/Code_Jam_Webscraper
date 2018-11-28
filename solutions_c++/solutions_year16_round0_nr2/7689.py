#include <iostream>
#include <cstring>
using namespace std;

int ans, now;
string st;
int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        cin >> st; ans = 0; now = 0;
        if (st[0] == '-') --ans;
        while (now < st.size()) {
            while ((now < st.size()) && (st[now] == '+')) ++now;
            if (now == st.size()) break;
            ++ans;
            while ((now < st.size()) && (st[now] == '-')) ++now;
            ++ans;
        }
        cout << ans << endl;
    }
    return 0;
}
