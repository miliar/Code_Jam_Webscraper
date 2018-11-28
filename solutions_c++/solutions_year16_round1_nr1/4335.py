#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int j = 1; j <= t; ++j) {
        string word;
        cin >> word;

        int n = word.size();
        string ans;
        for (int i = 0; i < n; ++i) {
            if (word[i] >= ans[0]) {
                ans = word[i] + ans;
            } else {
                ans = ans + word[i];
            }
        }
        cout << "Case #" << j << ": " << ans << "\n";
    }

    return 0;
}
