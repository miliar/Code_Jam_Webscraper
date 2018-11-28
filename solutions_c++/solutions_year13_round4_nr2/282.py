#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    long long cs;
    cin >> cs;
    for (int c = 1; c <= cs; c++)
    {
        long long n, p;
        cin >> n >> p;
        long long ans1 = (1LL << n) - 1LL, ans2 = 0LL;
        for (long long i = 0LL; i <= n; i++)
        {
            long long tmp = (1LL << n) - (1LL << (n - i)) + 1LL;
            //cout << i + 1 << " " << tmp << endl;
            if (tmp > p)
            {
                ans1 = (1LL << i) - 2LL;
                break;
            }
        }
        for (long long i = 0LL; i <= n + 1LL; i++)
        {
            if ((1LL << i) > p)
            {
                ans2 = (1LL << n) - (1LL << (n - i + 1LL));
                break;
            }
        }
        cout << "Case #" << c << ": " << ans1 << " " << ans2 << endl;
    }
    return 0;
}

