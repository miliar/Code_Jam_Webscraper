#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

const long long arr[39] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};

int T;
long long a, b;

int main() {
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> a >> b;
        int s = 0, e = 0;
        for (s = 0; s < 39; s++)
            if (arr[s] * arr[s] >= a)
                break;
        for (e = 0; e < 39; e++)
            if (arr[e] * arr[e] > b)
                break;

        cout << "Case #" << cas << ": " << e - s << endl;
    }
    return 0;
}
