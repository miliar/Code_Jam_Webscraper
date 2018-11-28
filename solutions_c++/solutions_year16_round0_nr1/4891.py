#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i++)  {
        long long int n;
        cin >> n;
        bool get[10] = { false, };

        long long int res = -1;
        long long int num = 0;
        for (int j = 0; j < 1000000; j++) {
            num += n;
            long long int d = num;
            while (d > 0) {
                get[d % 10] = true;
                d /= 10;
            }
            bool flag = true;
            for (int k = 0; k < 10; k++) {
                if (get[k] == false)
                    flag = false;
            }
            if (flag) {
                res = num;
                break;
            }
        }

        if (res == -1)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else
            cout << "Case #" << i << ": " << res << endl;
    }
}