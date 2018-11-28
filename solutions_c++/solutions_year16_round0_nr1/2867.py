#include <iostream>
#include <string>
#include <algorithm>
typedef long long LL;
using namespace std;

const int MAXN = 10000 + 10;

int main () {
	int cases;
	cin >> cases;

	for (int tc = 1; tc <= cases; tc ++) {
	    cout << "Case #" << tc << ": ";
        LL N;
        cin >> N;
        if (N == 0) {
            cout << "INSOMNIA" << endl;
        } else {
            int digits = 0;
            for (int j = 1; ; j ++) {
                LL d = j * N;
                while (d > 0) {
                    digits |= 1<< (d % 10);
                    d /= 10;
                }
                if (digits == (1 << 10) - 1) {
                    cout << j * N << endl;
                    break;
                }
            }
        }
    }
}
