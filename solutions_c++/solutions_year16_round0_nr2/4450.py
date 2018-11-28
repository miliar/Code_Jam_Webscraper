#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, NT;
    string s;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cin>>s;
        int res=0;
        for(int i=1; i<s.size(); ++i) {
            res += (s[i] != s[i-1]);
        }
        res += (s[s.size()-1] == '-');
        printf("Case #%d: %d\n", T, res);
    }
    return 0;
}
