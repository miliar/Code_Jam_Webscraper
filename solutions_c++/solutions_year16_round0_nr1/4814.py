#include <iostream>

using namespace std;

void getSheep(int n) {
    if (n==0)
        cout << "INSOMNIA\n";
    else {
        int num[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512};
        int see = 0;
        int j = 0;
        do {
            j++;
            int x = j * n;
            while (x > 9) {
                see = see | num[x % 10];
                x = x / 10;
            }
            see = see | num[x];
        } while (see < 1023);
        cout << j*n << "\n";
    }
}

int main() {
    int t, n;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> n;
        cout << "Case #" << i+1 << ": "; getSheep(n);
    }
    return 0;
}
