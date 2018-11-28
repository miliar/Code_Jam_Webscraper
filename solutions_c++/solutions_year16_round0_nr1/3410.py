#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int test_nr)
{
    int n;
    cin >> n;

    vector<bool> seen_digits(10, false);
    int count = 0;
    unsigned long long curr = n;
    unsigned long long prev;
    bool found_all_digits = false;

    while (! found_all_digits)
    {
        prev = curr;
        while (curr) {
            int last_digit = curr % 10;
            if (seen_digits[last_digit] == false)
            {
                if (count == 9)
                {
                    found_all_digits = true;
                    break;
                }
                seen_digits[last_digit] = true;
                count ++;
            }
            curr /= 10;
        }

        curr = prev + n;
        if (curr == n) // todo change
            break; // insomnia
    }

    cout << "Case #" << test_nr << ": ";
    if (found_all_digits)
        cout << prev << endl;
    else
        cout << "INSOMNIA" << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i ++) {
        solve(i);
    }

    return 0;
}
