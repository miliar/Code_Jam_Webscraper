#include <bits/stdc++.h>

using namespace std;

vector<char> V;

int main() {
    int t, tcase = 0;
    cin >> t;
    while (t--) {
        printf("Case #%d: ", ++tcase);
        V.clear();
        string tmp;
        cin >> tmp;
        V.push_back(tmp[0]);
        for (int i = 1; i < tmp.length(); i++) {
            if (tmp[i] != V[V.size() - 1]) {
                V.push_back(tmp[i]);
            }
        }
        int len = V.size();
        if (len == 1) {
            if (V[0] == '-') cout << "1" << endl;
            else cout << "0" << endl;
        }
        else {
            if (len % 2 == 0) {
                if (V[0] == '-') cout << len - 1 << endl;
                else cout << len << endl;
            } else {
                if (V[0] == '-') cout << len << endl;
                else cout << len - 1 << endl;
            }
        }
    }
    return 0;
}