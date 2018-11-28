#include <iostream>
#include <string>

using namespace std;

const int MAXS = 1000;
int T;

int main() {
    cin >> T;
    for (int i=0; i<T; i++) {
        int S;
        string v;
        cin >> S >> v;
        int tot = 0, nec = 0;
        for (int j=0; j<=S; j++) {
            if (tot < j) {
                nec += (j - tot);
                tot += (j - tot);
            }
            tot += (int)(v[j] - '0');
        }
        cout << "Case #" << (i+1) << ": " << nec << '\n';
    }
    return 0;
}
