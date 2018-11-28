#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, ca = 1;
    cin >> T;
    while(T--) {
        string s;
        cin >> s;
        int n = s.length();
        int ret = 0;
        for(int i = 1; i < n; i++) {
            if(s[i] != s[i - 1]) {
                ret++;
            }
        }
        if(s[n - 1] == '-') {
            ret++;
        }
        cout << "Case #" << ca << ": " << ret << endl;
        ca++;
    }
    return 0;
}
