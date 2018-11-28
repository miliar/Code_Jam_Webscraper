#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int x, fr[10], k = 0, a[100001];
        for (int j = 0; j <= 9; j++) fr[j] = 0;
        cin >> x;
        if (x == 0) cout << "Case #" << i << ": INSOMNIA" << "\n";
        else
            while (++k) {
                int mem = x, len= 0;
                while (mem > 0) {
                    a[++len] = mem % 10;
                    mem /= 10;
                }
                int save = 0, pointer = 0;
                for (int o = 1; o <= len; o++) {
                    if (pointer  == 0)
                        a[o] = a[o]*k + save;
                    else a[o] = save;
                    if (a[o] >= 10) {
                        save = a[o] / 10;
                        a[o] %= 10;
                        if (o == len) {
                            len++;
                            pointer = 1;
                        }
                    }
                    else save = 0;
                }
                for (int o = 1; o <= len; o++)
                    fr[a[o]] = 1;
                bool ver = true;
                for (int o = 0; o <= 9; o++)
                    if (fr[o] == 0) ver = false;
                if (ver == true) {
                    cout << "Case #" << i << ": ";
                    for (int o = len; o >= 1; o--) cout << a[o];
                    cout << "\n";
                    break;
                }
            }
    }
    return 0;
}
