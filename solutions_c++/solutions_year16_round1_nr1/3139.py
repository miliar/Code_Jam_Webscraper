#define ll long long
#include <bits/stdc++.h>
using namespace std;

template<class X>void debug(vector<X>&v){for(int i=0;i<v.size();i++)cout<<v[i]<<" ";cout<<endl;}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;

    for(int cs = 1; cs<=T; cs++) {
        printf("Case #%d: ", cs);
        string s, s1="", s2, s3;
        cin >> s;

        for(int i=0; s[i]; i++) {
            if(!i) {
                s1 += s[i];
                continue;
            }
            s2 = s1+s[i];
            s3 = s[i]+s1;
            s1 = max(s2, s3);
        }
        cout << s1 <<endl;
    }

    return 0;
}
