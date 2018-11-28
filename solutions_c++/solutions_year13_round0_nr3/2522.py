#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<long long> v;

int main() {
    for(int i = 1; i <= 10000000; ++i) {
        stringstream os;
        os << i;
        string s;
        os >> s;
        string ss = s;
        reverse(ss.begin(), ss.end());
        if (ss == s) {
            long long z = i;
            z *= i;
            stringstream oos;
            oos << z;
            oos >> s;
            ss = s;
            reverse(ss.begin(), ss.end());
            if (ss == s) {
                v.push_back(z);
            }
        }
    }
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t) {
        long long A, B;
        int ans = 0;
        cin >> A >> B;
        for(int i = 0; i < v.size(); ++i) {
            if (v[i] >= A && v[i] <= B) {
                ++ans;
            }
        }
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
}
