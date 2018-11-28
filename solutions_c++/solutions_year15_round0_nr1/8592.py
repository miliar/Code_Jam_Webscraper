#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int case_no = 1; case_no <= t; ++case_no) {
        int s;
        string a_str;
        cin >> s >> a_str;
        vector<int> a(s + 1, 0);
        vector<int> d(s + 1, 0);
        int curr_sum = a_str[0] - '0';
        for (int i = 1; i <= s; ++i) {
            a[i] = a_str[i] - '0';            
            if (a[i] == 0)
                continue;
            if (i > curr_sum) {
                d[i] = i - curr_sum;
            }
            curr_sum += d[i] + a[i];
        }
        cout << "Case #" << case_no << ": " << accumulate(d.begin(), d.end(), 0) << endl;
    }
    return 0;
}
