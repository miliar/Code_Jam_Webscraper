#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int cas = 1; cas <= n; cas++) {
        int a, b, cont = 0, num;
        cin >> a;
        vector <bool> v(17);
        for (int i = 0; i < 16; i++) {
            int x;
            cin >> x;
            if (i/4 + 1 == a) v[x] = true;
        }
        cin >> b;
        for (int i = 0; i < 16; i++) {
            int x;
            cin >> x;
            if (i/4 + 1 == b and v[x] == true) {
                cont++;
                num = x;
            }
        }
        cout << "Case #" << cas << ": ";
        if (cont == 0) cout << "Volunteer cheated!" << endl;
        if (cont == 1) cout << num << endl;
        if (cont > 1) cout << "Bad magician!" << endl;
    }
}