#include <iostream>

using namespace std;

bool check(bool seen[], int &count, int num)
{
    while (num) {
        int n = num % 10;
        if (!seen[n]) {
            seen[n] = true;
            count++;
        }
        num /= 10;
    }

    return count == 10;
}

int main()
{
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        bool seen[] = {false, false, false, false, false, false, false, false, false, false, };
        int count = 0;

        cout << "Case #" << i + 1 << ": ";
        if (n == 0) {
            cout << "INSOMNIA";
        } else {
            int sum = n;
            while (!check(seen, count, sum)) {
                sum += n;
            }
            cout << sum;
        }

        cout << endl;
    }
    return 0;
}
