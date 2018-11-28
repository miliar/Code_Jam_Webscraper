#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int c_to_i(char c)
{
    return c - '0';
}

int friends_needed(int max_level, string data)
{
    int ans = 0;
    int cur_standing = 0;

    if (max_level == 0) {
        return 0;
    }

    for (int i = 0; i < data.size(); ++i) {
        // cout << "cur_standing: " << cur_standing << endl;
        // cout << "ans: " << ans << endl;
        int si = c_to_i(data[i]);
        int cur_needed = cur_standing < i ? i - cur_standing : 0;
        cur_standing += cur_needed + si;
        ans += cur_needed;
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test_cases_num = 0;
    cin >> test_cases_num;
    for (int i = 0; i < test_cases_num; i++) {
        // cout << "starting Case #" << (i + 1) << "..." << endl;
        int max_level;
        string s;
        cin >> max_level >> s;
        cout << "Case #" << (i + 1) << ": " << friends_needed(max_level, s) << endl;
    }

    return 0;
}
