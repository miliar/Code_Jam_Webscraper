#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main ()
{
    int T;
    cin >> T;

    for (int Ti = 1; Ti <= T; Ti++) {
        int Smax;
        cin >> Smax;

        string str;
        cin >> str;

        int sum = 0;

        int ans = 0;
        for (int i = 0; i <= Smax; i++) {
            if (i > sum) {
                ans += i - sum;
                sum = i;
            }
            sum += (str[i] - '0');
        }
        cout << "Case #" << Ti << ": " << ans << endl;
    }
    return 0;
}
