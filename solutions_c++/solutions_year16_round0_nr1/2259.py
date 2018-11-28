#include <iostream>
using namespace std;

long evaluate(long n) {

    long arr[10] = {0};
    long count = 0, lastSeen;
    for (long sn = 1; count < 10; sn++) {
        lastSeen = n * sn;
        for (long n1 = lastSeen; n1; n1/=10) {
            long x = n1%10;
            count += (arr[x] ^ 1);
            arr[x] = arr[x] | 1;
        }
    }
    return lastSeen;
}

int main() {
    
    long T, n;
    cin >> T;
    for (long i = 1; i <= T; ++i) {
        cin >> n;
        cout << "Case #" << i << ": ";
        if (n == 0) {
            cout << "INSOMNIA";
        } else {
            cout << evaluate(n);
        }
        cout << "\n";
    }
}
