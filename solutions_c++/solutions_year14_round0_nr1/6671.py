#include <iostream>
#include <set>
#include <vector>

using namespace std;

const string BAD = "Bad magician!";
const string CHEAT = "Volunteer cheated!";


#define TASK "test"

int main() {
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        printf("Case #%d: ", t);
        int r;
        cin >> r;
        r--;
        set<int> s;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                int x;
                cin >> x;
                if (i == r)
                    s.insert(x);
            }
        cin >> r;
        r--;
        vector<int> ans;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                int x;
                cin >> x;
                if (i == r && s.count(x))
                    ans.push_back(x);
            }
        if (ans.size() == 1)
            cout << ans[0] << endl;
        if (ans.size() < 1)
            cout << CHEAT << endl;
        if (ans.size() > 1)
            cout << BAD << endl;
    }
    return 0;
}