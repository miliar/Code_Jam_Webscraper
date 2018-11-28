#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>

using namespace std;

int n;

int main()
{
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i) {
        string str;
        cin >> str;

        int flips = 0;
        while (true) {
            char first = str[0]; int j;
            for (j = 1; j < str.length(); ++j) {
                if (str[j] != first) {
                    break;
                }
            }

            if (j < str.length()) {
                for (int k = 0; k < j; ++k) {
                    if (str[k] == '-') str[k] = '+';
                    else str[k] = '-';
                }

                reverse(str.begin(), str.begin() + j);
                // cout << str << endl;

                flips++;
            }

            first = str[0]; bool ok = true;
            for (int k = 1; k < str.length(); ++k) {
                if (str[k] != first)
                    ok = false;
            }

            if (ok) {
                if (first == '-') flips++;
                break;
            }
        }

        printf("Case #%d: %d\n", i, flips);
    }
    return 0;
}
