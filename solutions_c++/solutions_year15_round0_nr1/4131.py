#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    char d[2];
    d[1] = 0;
    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        int s;
        cin >> s;
        int count = 0;
        int balance = 0;
        for (int i = 0; i <= s; ++i) {
            if (balance < i) {
                count += i - balance;
                balance += i - balance;
            }
            cin >> d[0];
            int v = atoi(d);
            balance += v;
        }
        cout << "Case #" << c << ": " << count << endl;
    }
    return 0;
}
