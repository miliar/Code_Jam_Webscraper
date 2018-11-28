#include <bits/stdc++.h>

using namespace std;

int main()
{
    int test_num;
    cin >> test_num;
    for (int i =0; i < test_num; i++) {
        set<int> was;

        long long initial;
        cin >> initial;

        int coeff = 0;
        for (int k = 1; k < 1000; k++) {
            long long buf = k * initial;
            while (buf) {
                was.insert(buf % 10);
                buf /= 10;
            }
            if (was.size() == 10) {
                coeff = k;
                break;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (not coeff) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << coeff * initial << endl;
        }
    }
}
