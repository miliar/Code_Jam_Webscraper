#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    int t, i;
    cin >> t;
    for (i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";

        string s;
        cin >> s;

        string r = "";
        r.insert(r.begin(), s[0]);
        for (auto c = s.begin() + 1; c != s.end(); c++) {
            if (*c >= *r.begin()) {
                r.insert(r.begin(), *c);
            } else {
                r.insert(r.end(), *c);
            }
        }
        cout << r;

        cout << endl;
    }
    return 0;
}
