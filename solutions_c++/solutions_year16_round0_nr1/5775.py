#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    long long t;
    long long n;

    vector<bool>m;
    string temp;
    long long count;
    long long ans;

    cin >> t;
    for (int i = 0; i < t; ++i) {
        ans = 0;
        count = 0;
        m.assign(10, false);
        cin >> n;
        if (n == 0) {
            cout << "Case #" + to_string(i + 1) << ": INSOMNIA" << endl;
            continue;
        }

        while (count != 10)
        {
            ++ans;
            temp = to_string(n * ans);
            for (int j = 0; j < temp.length(); ++j) {
                if (m[temp[j] - '0'] == false) {
                    m[temp[j] - '0'] = true;
                    ++count;
                }
            }
        }
        cout << "Case #" + to_string(i + 1) << ": " << n * ans << endl;
    }

    return 0;
}