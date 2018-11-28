#include <algorithm>
#include <iostream>

using namespace std;

#define MAXN 10000

int n;
int x;
int files[MAXN];

int solve()
{
    cin >> n >> x;
    for (int i = 0; i < n; ++i)
        cin >> files[i];
    sort(files, files + n);
    
    int ret = 0;
    int li = 0;
    int hi = n;
    while (li < hi)
    {
        int i1 = li;
        int i2 = hi - 1;
        if (i1 == i2)
        {
            ++ret;
            break;
        }
        if ((files[i2] + files[i1]) <= x)
        {
            ++li; --hi;
            ++ret;
        }
        else
        {
            --hi;
            ++ret;
        }
    }
    return ret;
}

int main()
{
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}