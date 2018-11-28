#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large_output.txt", "w", stdout);
    int t;
    cin >> t;
    int tc = 1;
    while(t--) {
        string s;
        cin>>s;
        int prev = 0;
        int n = s.size();
        int flag = 0;
        int i = 0;
        int answer = 0;
        if( s == "-") {
            answer = 1;
        } else {
            if( s[0] == '+') {
                for(int i = 1; i < n; i++) {
                    if(s[i] == '-' && s[i-1] == '+')
                        answer+=2;
                }
            }else if( s[0] == '-') {
                answer = 1;
                int bol = 0;
                for(int i = 1; i < n; i++) {
                    if(s[i] == '-' && s[i-1] == '+')
                        answer+=2;
                }
            }

        }
        cout << "Case #"<<tc<<": " << answer << endl;
        tc++;
    }

    return 0;
}
