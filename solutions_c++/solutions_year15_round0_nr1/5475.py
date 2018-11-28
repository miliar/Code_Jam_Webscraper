#include <bits/stdc++.h>

using namespace std;
#define s(x) scanf("%d", &x)
int main()
{
    freopen ("out.txt","w",stdout);
    freopen("inp.txt", "r", stdin);
    int t, z;
    s(t);

    for (z = 1; z <= t; z++) {
        int n, i;
        s(n);

        string s;
        cin >> s;
        int shy = 0, cnt = 0;
        shy = s[0] - '0';
        if (shy == 0) {
            shy = 1;
            cnt = 1;
        }
        for (i = 1; i < s.size(); i++) {
            int x = s[i] - '0';
            //cout << x << endl;
            if (x != 0) {
                if (shy < i) {
                    cnt += (i - shy);
                    shy += (i - shy);
                }
                shy += x;
            }
        }
        cout << "Case #" << z <<": ";
        cout << cnt << endl;
    }

    return 0;
}
