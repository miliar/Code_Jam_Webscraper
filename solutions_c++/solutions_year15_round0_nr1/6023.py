#define LARGE
//#define SMALL

#include <iostream>
#include <string>
using namespace std;

int it, tt;
int smax, scur, res, i;
string s;

int main()
{
#if defined(LARGE)
    freopen("../A-large.in", "r", stdin);
    freopen("../A-large.out", "w", stdout);
#elif defined(SMALL)
    freopen("../A-small-attempt0.in", "r", stdin);
    freopen("../A-small.out", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
#endif

    cin >> tt;

    for (it = 1; it <= tt; ++it)
    {
        cin >> smax >> s;
        res = 0;
        scur = 0;
        for (i = 0; i < s.size(); ++i)
        {
            if (scur > smax) break;
            if (scur < i)
            {
                ++scur;
                ++res;
            }
            scur += int(s[i]-'0');
        }
        cout << "Case #" << it << ": " << res << endl;
    }

    return 0;
}
