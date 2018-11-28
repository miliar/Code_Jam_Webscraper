#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

long long n,t;
long long a[100000];
long long ans = 1e9;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (long long k = 1; k <= t; ++k)
    {
        ans = 1e9;
        cin >> n;
        for (long long i = 0; i < n; ++i)
            cin >> a[i];
        for (long long p = 1; p <= 2005; ++p)
        {
            long long cur_ans = p;
            for (long long i = 0; i < n; ++i)
                if (a[i] > p)
                    cur_ans += a[i]/p + ((a[i]%p == 0)?0:1) - 1;
            ans = min(ans, cur_ans);
        }
        cout << "Case #" << k << ": " << ans << endl;
    }
}
