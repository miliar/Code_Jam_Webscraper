#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int B;
int M[1000];

long served(long tim) {
    long num = 0;
    for (int i = 0; i < B; i++) {
        num += tim / M[i] + 1;
    }
    return num;
}

long search(long n, long a, long b) {
    while (a < b) {
        long m = (a + b) / 2;
        //cerr << a << " " << m << " " << b << endl;
        //cerr << served(m) << " " <<  n << endl;
        if (served(m) < n) a = m + 1;
        else b = m;
        //cerr << a << " " << m << " " << b << endl << endl;
        //cout << a << " " << b << endl;
    }
    return a;
}

int main() {
    int T, N;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long N;
        cin >> B >> N;
        for (int i = 0; i < B; i++) cin >> M[i];
        long tim = search(N, 0, 1000000000000000L);
        long num = 0;
        for (int i = 0; i < B; i++) {
            num += (tim - 1) / M[i] + 1;
        }
        //cout << num << " " << tim << endl;
        int b;
        for (b = 0; b < B; b++) {
            if (tim % M[b] == 0) num++;
            if (num == N) break;
        }
        //cout << num << endl;
        if (b + 1 <= 0 or b + 1 > B) cerr << "DANGER!!!" << endl;
        if (!(served(tim - 1) < N and served(tim) >= N)) cerr << "DANGER!!!" << endl;
        //cerr << tim << endl;
        //cerr << N << " " << served(tim - 1) << " " << served(tim) << endl;
        //cerr << B << " " << b + 1 << endl;
        cout << "Case #" << t << ": " << b + 1 << endl;
    }
}
