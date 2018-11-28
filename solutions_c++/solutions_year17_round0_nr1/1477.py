#include<iostream>
using namespace std;
void p(int _) {
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    for(int i = 0; i <= s.size() - k; i ++) {
        if(s[i] == '-') {
            for(int j = i;j < i + k; j ++) {
                if(s[j] == '+') s[j] = '-';
                else    s[j] = '+';
            }
            ans ++;
        }
    }
    cout << "Case #" << _ << ": ";
    for(int i = s.size() - k; i < s.size(); i ++)
        if(s[i] == '-') {
            cout << "IMPOSSIBLE";
            return;
        }
    cout << ans;
    return;
}
int main() {
    int t;
    cin >> t;
    for(int i = 0; i < t; i ++) {
        p(i + 1);
        cout << endl;
    }
}
