#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string order = "8024675139";
    vector <string> names = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

    for (int tst = 0; tst < T; tst++) {
        string s;
        cin >> s;
        multiset <char> all;
        vector <int> res;

        for (char c: s) {
            all.insert(c);
        }

        for (int i = 0; i < 10; i++) {
            int num = order[i] - '0';
            string name = names[num];

            while (true) {
                int pos;

                for (pos = 0; pos < int(name.size()); pos++) {
                    if (all.count(name[pos])) {
                        all.erase(all.find(name[pos]));
                    } else {
                        for (pos = pos - 1; pos >= 0; pos--) {
                            all.insert(name[pos]);
                        }
                        break;
                    }
                }

                if (pos == int(name.size())) {
                    res.push_back(num);
                } else {
                    break;
                }
            }
        }
        cout << "Case #" << tst + 1 << ": ";
        sort(res.begin(), res.end());

        for (int x: res) {
            cout << x;
        }
        cout << '\n';
    }
}
