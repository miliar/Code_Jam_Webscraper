#include <fstream>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    ifstream cin("input");
    ofstream cout("output.txt");
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        string s;
        cin >> s;
        vector <int> arr(t + 1);
        for (int j = 0; j <= t; j++)
            arr[j] = s[j] - '0';
        int cur = 0, ans = 0;
        for (int j = 0; j <= t; j++) {
            ans += max(0, j - cur);
            cur = max(cur, j);
            cur += arr[j];
        }
        cout << "Case #" << i + 1 << ": " << ans << "\n";
    }
    return 0;
}
