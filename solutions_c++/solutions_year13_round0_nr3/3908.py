#include <cstdio>
#include <iostream>

using namespace std;

bool pal(int x) {
    int a = x, y = 0;
    while (a > 0) {
        y = 10 * y + a % 10;
        a /= 10;
    }
    return x == y;
}

int p[1001];


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int i;
    for (i = 1; i <= 33; i++)
        if (pal(i) && pal(i*i)) p[i*i] = 1;

    for (i = 1; i <= 1000; i++) p[i] += p[i-1];

    int T, A, B;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cin >> A >> B;
        cout << "Case #" << tc << ": " << p[B] - p[A-1] << endl;
    }

}
