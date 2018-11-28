#include <iostream>
#include <sstream>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(6);

    for (int test = 1; test <= T; ++test) {
        int n;
        cin >> n;

        if (n) {
            int next = 0, digs = 0;
            vector<int> mark(10, 0);

            while (digs < 10) {
                next += n;
                int t = next;
                while (t) {
                    int digit = t % 10;
                    t /= 10;
                    if (!mark[digit]) {
                        digs++;
                        mark[digit] = 1;
                    }
                }
            }

            if (digs == 10) {
                cout << "Case #" << test << ": " << next << endl;
            }
        }
        else {
                cout << "Case #" << test << ": INSOMNIA" << endl;
        }
    }

    return 0;
}
