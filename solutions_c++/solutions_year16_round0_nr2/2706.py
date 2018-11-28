#include <iostream>
using namespace std;

int solve(string st) {
    if (st.find("+") == -1) return 1;
    if (st.find("-") == -1) return 0;
    int res = 1;
    for (int i = 1; i < st.size(); i++) {
        if (st[i] != st[i - 1]) ++res;
    }
    if (st[st.size() - 1] == '+') --res;
    return res;
}

int main() {
    freopen("B.in", "r", stdin);
    int ca;
    string st;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        cin >> st;
        printf("Case #%d: %d\n", i + 1, solve(st));
    }
    return 0;
}
