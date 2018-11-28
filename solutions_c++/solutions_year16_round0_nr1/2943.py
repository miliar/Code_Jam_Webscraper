#include <iostream>

using namespace std;

int main() {
    
    int casen;
    cin >> casen;
    casen = 0;
    
    long long n;
    while (cin >> n) {
        casen++;
        cout << "Case #" << casen << ": ";
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        int bm = 0;
        long long c = 0;
        while (bm != 1023) {
            c++;
            long long cn = c * n;
            while (cn > 0) {
                bm |= 1 << (cn%10);
                cn /= 10;
            }
        }
        cout << c*n << endl;
    }

}
