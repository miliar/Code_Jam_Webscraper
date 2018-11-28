#include <bits/stdc++.h>

using namespace std;

int main()
{
    int i, t, j, k, n, l, cnt;
    freopen ("B-large.in", "r", stdin);
    freopen("output1.txt", "w", stdout);
    cin>>t;
    string s, tmp;

    for (j = 1; j <= t; j++) {
        cin>>s;
        cnt = 0;
        while (1) {
            k = -1;
            for (i = 0; i < s.length(); i++) {
                if (s[i] == '-') {
                    k = i;
                }
            }
            if (k == -1) {
                cout<<"Case #"<<j<<": "<<cnt<<endl;
                break;
            }
            else {
                cnt++;
                for (i = 0; i <= k; i++) {
                    s[i] = s[i] == '+' ? '-' : '+';
                }
            }
        }
    }

    return 0;
}
