#include <fstream>
#include <iostream>
using namespace std;
fstream fsi("in.txt", fstream::in);
fstream fso("out.txt", fstream::out);

void printBinary(int a) {

}

void solve() {
    int i, j, t;
    string a, b;
    fsi >> t;
    for (i = 1; i <= t; i++) {
        fsi >> a;
        b = a[0];
        for (j = 1; j < a.size(); j++) {
            if (b[0] <= a[j]) {
                b = a[j]+b;
            } else {
                b = b+a[j];
            }
        }
        fso << "Case #" << i << ": " << b << '\n';
    }
}

int main() {
    solve();
    return 0;
}
