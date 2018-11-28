#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

long long f(long long pos, long long len, long long base, int c) {
    if (c == 1) {
        return pos;
    } else {
        return f((pos - 1) * base + 1, len * base, base, c - 1);
    }
}

int main(int argc, char *argv[])
{
    int T = 0;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        long long K = 0, C = 0, S = 0;
        cin >> K >> C >> S;

        cout << "Case #" << cas << ":";
        for (int i = 1; i <= S; i++) {
            cout << " " << f(i, K, K, C);
        }
        cout << endl;
    }
    return 0;
}
