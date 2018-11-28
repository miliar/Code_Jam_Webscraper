#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int t, cou = 1, i;
    cin >> t;
    while(t--) {
        char s[1001], be, en;
        cin >> s;
        string res;
        res = s[0];
        be = en = s[0];
        i = 1;
        cout << "Case #" << cou++ << ": ";
        while(s[i] != '\0') {
            if(s[i]>=be) {
                res.insert(res.begin(), s[i]);
                be = s[i];
            }
            else {
                res += s[i];
                en = s[i];
            }
            i++;
        }
        cout << res << endl;
    }
    return 0;
}
