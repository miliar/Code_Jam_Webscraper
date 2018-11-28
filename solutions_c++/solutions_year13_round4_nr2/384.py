#include <iostream>
#include <cstdio>
using namespace std;
long long n, m;

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
        cout << "Case #" << tt << ": ";
        cin >> n >> m;
        if (m == 1LL << n) {
            cout << (1LL << n) - 1LL << ' ' << (1LL << n) - 1LL << endl;
            continue;
        }
        //long long l = n - 1;
        long long p = m, i = n;
        while (p > 0) {
            i--;
            p -= 1LL << i;
        }
        cout << (1LL << (n-i)) - 2 << ' ';
        long long n1 = 1LL << n, m1 = 1LL << n;
		i = n;
		while (n1 > m)
		{
			--i;
			n1 -= 1LL << i;
		}
		m1 -= 1LL << (n-i);
		cout << m1 << endl;
        //for (int i = 1; i <=
    }
    return 0;

}

