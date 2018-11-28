#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

bool occur[16] = {0};

long long solve(int num) {
    if (num == 0) {
        return -1;
    }
    memset(occur, 0, sizeof(occur));
    int remain = 10;
    long long res = -1;
    for (int i = 1; i <= 1000000; i++) {
        long long x = 1LL * num * i;
        long long mul = x;
        while (x > 0) {
            if (occur[x % 10] == false) {
                occur[x % 10] = true;
                remain--;
            }
            x /= 10;
        }

        if (remain == 0) {
            res = mul;
            break;
        }
    }

    return res;
}

int main(int argc, char *argv[])
{
    int T = 0;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        int num = 0;
        cin >> num;
        long long res = solve(num);
        cout << "Case #" << cas << ": ";
        if (res == -1) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << res << endl;
        }
    }
    return 0;
}
