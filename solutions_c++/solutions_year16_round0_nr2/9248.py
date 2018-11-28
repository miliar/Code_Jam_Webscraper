#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input13.in","r",stdin);
    freopen("output13.out","w",stdout);
    int t, i;
    string s;

    cin>>t;

    for (int x = 1; x <= t; x++) {
        cin>>s;

        s = s+'+';
        i = 0;
        int ans = 0;
        int c = 0;

        while (i < s.length()) {
            while (s[i] != '+') {
                i++;
                c++;
            }

            if (s[i] == '+') i++;
            if (c > 0) {
                ans++;
                break;
            } else break;
        }

        while (i < s.length()) {
            c = 0;

            while (s[i] != '+') {
                i++;
                c++;
            }

            if (s[i] == '+') i++;

            if (c > 0) ans += 2;
        }

        cout<<"Case #"<<x<<": "<<ans<<endl;
    }

    return 0;
}
