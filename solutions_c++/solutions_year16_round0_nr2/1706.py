#include<bits/stdc++.h>
using namespace std;
#define ll long long
template<class T> void debug(T v) {
    for(int i=0;i<(int)v.size();i++)cout << v[i] <<" ";cout<<endl;
}
template<class T> void input(T &v) {
    for(int i=0;i<(int)v.size();i++)cin>>v[i];
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    cin >> t;

    for(int cs = 1; cs <= t; cs++) {
        string s;
        cin >> s;
        char sign = s[0];
        int ans = 0;
        for(int i = 1; s[i]; i++) {
            if(sign != s[i]) {
                sign = s[i];
                ans++;
            }
        }
        if(sign=='-') ans++;
        printf("Case #%d: %d\n", cs, ans);
    }

    return 0;
}
