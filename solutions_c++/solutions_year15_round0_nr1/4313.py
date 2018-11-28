#include <iostream>
#include <string>

using namespace std;

int main ()
{
    int T;
    cin >> T;
    for (int j = 1; j <= T; ++ j)
    {
        int sMax;
        string s;
        long long sum = 0;
        long long ans = 0;
        cin >> sMax >> s;
        for (int i = 0; i < s.size (); ++ i)
        {
            if (sum < i)
            {
                ans += i - sum;
                sum += (i - sum);
            }
            sum += s [i] - '0';
        }
        cout << "Case #" << j << ": " << ans << '\n';
    }
    return 0;
}

