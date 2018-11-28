#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, ca = 1;
    cin >> T;
    while(T--) {
        string s;
        cin >> s;
        cout << "Case #" << ca << ": ";
        ++ca;
        deque<char> q;
        q.push_back(s[0]);
        for(int i = 1; i < s.length(); i++) {
            if(s[i] >= q.front()) {
                q.push_front(s[i]);
            } else {
                q.push_back(s[i]);
            }
        }
        for(int i = 0; i < q.size(); i++) {
            cout<<q[i];
        }
        cout << endl;
    }
    return 0;
}
