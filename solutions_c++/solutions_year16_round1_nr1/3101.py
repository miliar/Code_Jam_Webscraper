#include <iostream>
#include <string>
using namespace std;

string solve(string st) {
    string ret = st.substr(0, 1);
    for (int i = 1; i < st.length(); i++) {
        string temp1 = ret + st[i];
        string temp2 = st[i] + ret;
        if (temp1 > temp2) {
            ret = temp1;
        } else {
            ret = temp2;
        }
    }
    return ret;
}

int main() {
    int ca;
    string st;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        cin >> st;
        printf("Case #%d: %s\n", i + 1, solve(st).data());
    }
    return 0;
}
