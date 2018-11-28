#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int num;
        string s;
        cin >> num >> s;
        int ans(0), count(0);
        count += (int)(s[0] - '0');
        for (int j = 1; j <= num; j++) {
            if (count < j) {
                ans += j - count;
                count = j;
            }
            count += (int)(s[j] - '0');
        }
        cout << "Case #" << i <<": " << ans << endl;
    }
    return 0;
}