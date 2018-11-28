#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;


int main() {
    int nt, tc, i, j, k;
    char str[1002];
    char flipped[1001];

    cin >> nt;
    for (tc = 1; tc <= nt; tc++) {
        memset(flipped, 0, sizeof(flipped));
        cin >> str >> k;

        int count = 0;
        int f = 0;
        int len = strlen(str);
        for (i = 0; i < len; i++) {
            if (i >= k) f = f ^ flipped[i - k];
            if ((str[i] == '-') ^ f) {
                if (i + k > len) {
                    count = -1;
                    break;
                }
                flipped[i] = 1;
                count++;
                f = !f;
            }
        }
        cout << "Case #" << tc << ": ";
        if (count == -1) 
            cout << "IMPOSSIBLE" << endl;
        else
            cout << count << endl;
    }

    return 0;
}
