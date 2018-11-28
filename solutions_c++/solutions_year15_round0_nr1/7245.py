#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define ll long long
#define ull unsigned long long
#define inf INT_MAX
using namespace std;

int main() {_
    int T;
    cin >> T;
    int sm;
    string s;
    int friends, total;
    for(int $ = 1; $ <= T; ++ $) {
        friends = 0;
        cin >> sm;
        cin >> s;
        total = s[0] - '0';
        int x;
        for(int i = 1; i <= sm; ++ i) {
            if(s[i] != '0') {
                x = s[i] - '0';
                if(total < i) {
                    friends += i - total;
                    total += x + (i - total);
                } else
                    total += x;
            }
        }
        cout << "Case #" << $ << ": " << friends << endl;
    }
    return 0;
}
