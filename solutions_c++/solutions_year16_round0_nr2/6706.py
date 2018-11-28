#include <bits/stdc++.h>

using namespace std;

#define s(x) scanf("%d", &x)
#define ll long long

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, z = 1;
    s(t);

    string s;

    while (t--) {
        cin >> s;

        int n = s.size(), cnt = 0, i, f = 0;

        for (i = n-1; i >= 0; i--) {
            if (s[i] == '-')
                f = 1;
            else {
                if (f == 1) {
                    f = 0;
                    cnt += 2;
                }
            }
        }

        if (f == 1)
            cnt++;
        printf("Case #%d: ", z++);
        cout << cnt << endl;
    }
}
