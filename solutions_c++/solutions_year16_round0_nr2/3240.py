#include <bits/stdc++.h>

#define debug(x) cout << "> " << #x << " = " << x << endl;
#define debugat(arr, at) cout << "> " << #arr << "[" << at << "] = " << arr[at] << endl;

using namespace std;

string s;
int solve() {
    int ans = 0;
    int n = s.size();
    while(true) {
        int cont = 0;
        int i;
        for(i = 1; i < n and s[i] == s[i - 1]; ++i) {
        }
        if(i == n) {
            if(s[0] == '-')
                ++ans;
            return ans;
        }
        else {
            char next = (s[0] == '+' ? '-' : '+');
            for(int j = 0; j < i; ++j)
                s[j] = next;
            ++ans;
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;

    for(int t = 1; t <= n; ++t) {
        cin >> s;

        cout << "Case #" << t << ": " << solve() << "\n";
    }
    return 0;
}
