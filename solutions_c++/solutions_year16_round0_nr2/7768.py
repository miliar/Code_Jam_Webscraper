#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <cctype>
#include <algorithm>
using namespace std;

int calFlip(const vector<bool> &isHappy, int N) {
    if (N <= 1) {
        return 0;
    }
    bool lastState = isHappy[N - 1];
    int i = N - 2;
    while (i >= 0) {
        if (isHappy[i] != lastState) {
            break;
        }
        i--;
    }
    int numPrefix = 0;
    if (i >= 0) {
        numPrefix = calFlip(isHappy, i + 1) + 1;
    }
    return numPrefix;
}

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        string str;
        cin >> str;
        cout << "Case #" << i + 1 << ": ";

        int N = str.size();
        vector<bool> isHappy(N, false);
        for (int i = 0; i < N; i++) {
            if (str[i] == '+') {
                isHappy[i] = true;
            }
        }
        int cnt = calFlip(isHappy, N);
        if (isHappy[N - 1] == false) {
            cnt++;
        }
        cout << cnt << endl;
    }

    return 0;
}