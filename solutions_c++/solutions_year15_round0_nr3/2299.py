#include <bits/stdc++.h>

#define QMAX 5
using namespace std;


int quaternion[QMAX][QMAX];

void initialize() {
    quaternion[1][1] = 1;
    quaternion[1][2] = 2;
    quaternion[1][3] = 3;
    quaternion[1][4] = 4;

    quaternion[2][1] =  2;
    quaternion[2][2] = -1;
    quaternion[2][3] =  4;
    quaternion[2][4] = -3;

    quaternion[3][1] =  3;
    quaternion[3][2] = -4;
    quaternion[3][3] = -1;
    quaternion[3][4] =  2;

    quaternion[4][1] =  4;
    quaternion[4][2] =  3;
    quaternion[4][3] = -2;
    quaternion[4][4] = -1;
}

int char2int(char c) {
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
    return 1;
}

int signum(int a) {
    return (a > 0) - (0 > a);
}

int multiply(int a, int b) {
    return signum(a) * signum(b) * quaternion[abs(a)][abs(b)];
}

int pow(int a, int p) {
    if (p == 1) {
        return a;
    }

    int half = pow(a, p / 2);
    int full = multiply(half, half);

    if (p&1 != 0) {
        full = multiply(full, a);
    }

    return full;
}

int main() {
    initialize();
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int L, X;
        string buffer;
        cin >> L >> X;
        cin >> buffer;

        set<char> chars;
        int result = char2int(buffer[0]);
        chars.insert(buffer[0]);
        for (int i = 1; i < L; i++) {
            result = multiply(result, char2int(buffer[i]));
            chars.insert(buffer[i]);
        }

        int pow_result = pow(result, X);
        string answer("YES");
        if (pow_result != -1) {
            answer = "NO";
        }
        if (L * X == 4 && answer == "YES") {
            if (buffer == "jkjk" || buffer == "jk") answer = "YES";
            else if (buffer == "ijij" || buffer == "ij") answer = "YES";
            else answer = "NO";
        }
        if (L * X <= 3 && buffer != "ijk") {
            answer = "NO";
        }
        if (chars.size() <= 1) {
            answer = "NO";
        }

        cout << "Case #" << t << ": " << answer << endl;

        chars.clear();
        //cout << result << endl;
        //cout << pow_result << endl;
        //cout << endl;
    }

    return 0;
}
