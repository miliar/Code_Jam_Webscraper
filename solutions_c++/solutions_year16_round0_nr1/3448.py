#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
  //  t=1;
    long long a, n;
    for (int i = 1; i <= t; i++) {
        bool digits[10] = {false};
        cin >> a;
       // a = 1;
        if (a == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        n = a;
        int x = 1;
        while (true) {
            long long z = n;
            do {
                int digit = n % 10;
                digits[digit] = true;
                n /= 10;
            } while (n > 0);

            if (all_of(begin(digits), end(digits), [](bool f){return f;})) {
                cout << "Case #" << i << ": " << z << endl;
                break;
            } else {
                x++;
                n = a*x;
            }
        }
    }
    return 0;
}

