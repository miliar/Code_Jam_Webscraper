#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
string s;
int x;
int main() {
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    int tk=0;
    for (;t>=1;t--) {
        cin >> x >> s;
        int ans=0;
        x++;
        int q=s[0]-'0';
        for (int i=1;i<x;i++) {
            if (q>=i) q+=s[i]-'0';
            else {
                ans+=i-q;
                q+=i-q;
                q+=s[i]-'0';
            }
        }
        tk++;
        cout << "Case #" << tk << ": " << ans << "\n";
    }
    return 0;
}
