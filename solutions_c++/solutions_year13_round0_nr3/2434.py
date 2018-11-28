#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

typedef long long i64;
typedef vector<int> vi;

int fair[10000010];

bool isPalin(i64 n)
{
    char s[20];
    int l = 0;
    for (; n; n /= 10, ++l)
    {
        s[l] = n % 10 + '0';
    }

    for (int i = 0; i < l / 2; ++i)
    {
        if (s[i] != s[l - i - 1])
            return false;
    }
    return true;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    fair[0] = 0;
    for (i64 i = 1; i < 10000010; ++i)
    {
        if (isPalin(i) && isPalin(i * i))
        {
            fair[i] = fair[i - 1] + 1;
        }
        else
        {
            fair[i] = fair[i - 1];
        }
    }

    int t;
    cin >> t;
    for (int cnt = 1; cnt <= t; ++cnt)
    {
       i64 a, b;
       cin >> a >> b;
       printf("Case #%d: ", cnt);
       cout << fair[(int) sqrt((double) b)] - fair[(int) sqrt((double) a - 1)] << endl;
    }
    return 0;
}