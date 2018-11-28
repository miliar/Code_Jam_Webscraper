#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
string s;
int f[205][2];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int Tcas;
    cin >> Tcas;
    for (int T = 1; T <= Tcas; T++) {
        cin >> s;
        memset(f, 0, sizeof(f));
        for (int i = 1; i <= s.length(); i++) {
            if (s[i-1] == '+') {
                f[i][0] = f[i-1][0];
                f[i][1] = f[i-1][0] + 1;
            } else {
                f[i][0] = f[i-1][1] + 1;
                f[i][1] = f[i-1][1];
            }
        }
        cout << "Case #" << T << ": " << f[s.length()][0] << endl;
    }
}
