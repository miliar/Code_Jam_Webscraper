#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, n, x, y;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        string s;
        cin >> n >> s;

        x = 0;
        y = s[0] - '0';
        for (int j = 1; j < s.length(); ++j) {
            if (y < j) {
                x += j - y;
                y = j;
            }

            y += s[j] - '0';
        }

        cout << "Case #" << i << ": " << x << endl;
    }

    return 0;
}