#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
using namespace std;
typedef long long ll;

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        string S;
        cin >> S;
        deque<char> ret;
        ret.push_front(S[0]);
        for (int i = 1; i < S.size(); i++) {
            if (S[i] >= ret.front()) {
                ret.push_front(S[i]);
            } else {
                ret.push_back(S[i]);
            }
        }

        printf("Case #%d: ", t);
        for (char c : ret)
            cout << c;
        cout << endl;
    }

    return 0;
}
