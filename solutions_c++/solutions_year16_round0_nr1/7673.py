#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <cctype>
#include <algorithm>
using namespace std;

int checkDigits(const vector<bool> &isDigits) {
    int cnt = 0;
    for (auto b : isDigits) {
        if (b) {
            cnt++;
        }
    }
    return cnt;
}

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        long N;
        cin >> N;
        cout << "Case #" << i + 1 << ": ";
        if (N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        vector<bool> isDigits(10, false);
        long M = 0;
        while (checkDigits(isDigits) < 10) {
            M += N;
            long m = M;
            while (m > 0) {
                isDigits[m % 10] = true;
                m /= 10;
            }
        }
        cout << M << endl;
    }

    return 0;
}