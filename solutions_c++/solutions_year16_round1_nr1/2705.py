#include <bits/stdc++.h>

#define debug(x) cout << "> " << #x << " = " << x << endl;
#define debugat(arr, at) cout << "> " << #arr << "[" << at << "] = " << arr[at] << endl;

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int tests;
    cin >> tests;

    for(int t = 1; t <= tests; ++t) {
        string s;
        cin >> s;

        list<char> ans;
        ans.push_back(s[0]);
        for(int i = 1; i < (int) s.size(); ++i) {
            if(s[i] >= ans.front()) {
                ans.push_front(s[i]);
            }
            else {
                ans.push_back(s[i]);
            }
        }

        cout << "Case #" << t << ": ";
        for(char c : ans)
            cout << c;
        cout << "\n";
    }
    return 0;
}
