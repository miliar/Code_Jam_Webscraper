#include<bits/stdc++.h>
using namespace std;

int main() {
    freopen("out(large).txt", "w", stdout);
    int T, cs, str;
    string a, b;
    cin >> T;
    for(cs = 1; cs <= T; cs ++) {
        cin >> a;
        deque<char> dq;
        for(int i = 0; i < a.size(); i ++) {
            char ch = a[i];
            if(dq.empty()) {
                dq.push_back(ch);
                continue;
            }
            if(ch >= dq.front()) {
                dq.push_front(ch);
            } else {
                dq.push_back(ch);
            }
        }
        printf("Case #%d: ", cs);
        for(int i = 0 ; i < dq.size(); i ++) {
            cout << dq[i] ;
        }
        cout << endl;
    }
}
