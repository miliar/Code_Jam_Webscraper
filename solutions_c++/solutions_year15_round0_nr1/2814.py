#include <iostream>
#include <string>
using namespace std;

void real_main() {
    int s; string x;
    cin >> s >> x;

    int p = 0, a = 0;
    for (int i = 0; i <= s; i++) {
        int cur = x[i] - '0';
        if (p < i) {
            a += i-p; p = i;
        }
        p += cur;

    }
    cout << a << endl;
}

int main() {
    int t; cin >> t;
    for (int i = 1; i <=t; i++) {
        cout << "Case #" << i << ": ";
        real_main();
    }
    return 0;
}
