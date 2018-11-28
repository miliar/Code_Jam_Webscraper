#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, a, b, x;
    cin>>t;
    ll T = t;
    string s;
    deque<char> d;
    while(t--) {
        cin>>s;
        d.clear();
        d.push_back(s[0]);
        for (i=1; i<s.length(); i++) {
            if (s[i]>=d.front()) {
                d.push_front(s[i]);
            }
            else {
                d.push_back(s[i]);
            }
        }
        cout<<"Case #"<<(T-t)<<": ";
        for (deque<char>::iterator it = d.begin(); it!=d.end(); it++) {
            cout<<*it;
        }
        cout<<endl;

    }


    return 0;

}