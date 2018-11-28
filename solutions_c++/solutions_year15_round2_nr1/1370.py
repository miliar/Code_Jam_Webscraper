#include <cstdio>
#include <iostream>

using namespace std;

int T, n;
int ff[1000001];

int rev(int x) {
    int res = 0;
    while (x) {
        res *= 10;
        res += x % 10;
        x /= 10;
    }
    return res;
}

int q[10000007], f, r;

void BFS() {
    q[0] = 1; ff[1] = 1;
    for (int f = 0, r = 1; f < r; ++f) {
        if (q[f] > 1000000) continue;
        if (ff[q[f]+1] == 0) {
            ff[q[f]+1] = ff[q[f]] + 1;
            q[r++] = q[f]+1;
        }
        int rv = rev(q[f]);
        if (ff[rv] == 0) {
            ff[rv] = ff[q[f]] + 1;
            q[r++] = rv;
        }

    }
}

int main() {
    cin >> T;
    BFS();
    for (int cs = 1; cs <= T; ++cs) {
        cin >> n;
        cout << "Case #" << cs << ": " << ff[n] << endl;
    }
}
