#include <bits/stdc++.h>
using namespace std;

#define ing long long

#undef int
int main()
{
#define int long long
    int T;
    cin >> T;
    int kase = 0;
    while (T--) {
        cout << "Case #" << ++kase << ": ";
        string in;
        cin >> in;
        int k;
        cin >> k;
        int used = 0;
        bool ok = true;
        int ln = in.length();
        for (int i = 0; i < ln; i++) {
            if (in[i] == '-') {
                if (i + k > ln) {
                    ok = false;
                    break;
                }
                used++;
                for (int j = i; j < (i + k); j++) {
                    if (in[j] == '-')
                        in[j] = '+';
                    else
                        in[j] = '-';
                }
            }
        }
        if (ok) {
            cout << used << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
