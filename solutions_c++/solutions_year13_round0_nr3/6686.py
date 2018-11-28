#include <iostream>
#include <cmath>

using namespace std;

bool check(int a) {
    int b = 0, temp = a;
    while (a > 0) {
        b *= 10;
        b += a % 10;
        a /= 10;
    }
    return b == temp;
}

int main() {
    // The number of cases
    int T;
//    freopen("/Users/Sean/1.in", "r", stdin);
//    freopen("/Users/Sean/1.out", "w", stdout);

    cin >> T;
    for (int k = 0; k < T; k++) {
        int a, b, sum = 0;
        cin >> a >> b;
        for (int i = 1; i <= sqrt(b) + 1; i++) {
            if (check(i)) {
                if ((i * i <= b) && (i * i >= a) && check(i * i)) {
                    sum++;
                }
            }
        }
        cout << "Case #" << k + 1 << ": " << sum << endl;
    }

//    fclose(stdin);
//    fclose(stdout);
    return 0;
}

