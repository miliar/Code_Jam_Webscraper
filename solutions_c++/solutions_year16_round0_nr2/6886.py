#include <bits/stdc++.h>
using namespace std;
string s;
int T;

int flip(int r) {
    string temp = s;
    for(int i=0;i<r;i++) {
        if(temp[i] == '+') {
            s[r-i-1] = '-';
        } else {
            s[r-i-1] = '+';
        }
    }
    //cout << s << endl;
}

int solve(int idx) {
    if(idx==s.length()) return 0;
    int res = solve(idx+1);

    if(s[idx] == '+') return res;

    if(s[0] == '-') {
        flip(idx+1);
        return res+1;
    }

    for(int i=idx-1;i>=0;i--) {
        if(s[i] == '+') {
            flip(i+1);
            flip(idx+1);
            return res+2;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> T;
    for(int t=1;t<=T;t++) {
        cin >> s;
        cout << "Case #" << t << ": " << solve(0) << endl;;
    }
}
