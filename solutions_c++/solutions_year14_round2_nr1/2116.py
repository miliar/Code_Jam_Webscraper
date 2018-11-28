//#define LARGE
#define SMALL

#include <iostream>
#include <string>

using namespace std;

int it, tt;

string s[100];
string r, t;
int i, j, k, n, d[100][100], l[100], rl, ans, sum;
bool fw;

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

    for(it = 1; it <= tt; ++it)
    {
        cin >> n;

        cin >> s[0];
        l[0] = s[0].length();

        r = "";
        r.push_back(s[0][0]);
        k = 0;
        d[0][k] = 1;
        for(j = 1; j < l[0]; ++j)
        {
            if(s[0][j] != s[0][j-1])
            {
                d[0][++k] = 1;
                r.push_back(s[0][j]);
            }
            else
            {
                ++d[0][k];
            }
        }
        rl = r.length();
        
        fw = false;
        for(i = 1; i < n; ++i)
        {
            cin >> s[i];
            l[i] = s[i].length();

            if(!fw)
            {
                t = "";
                t.push_back(s[i][0]);
                k = 0;
                d[i][k] = 1;
                for(j = 1; j < l[i]; ++j)
                {
                    if(s[i][j] != s[i][j-1])
                    {
                        d[i][++k] = 1;
                        t.push_back(s[i][j]);
                    }
                    else
                    {
                        ++d[i][k];
                    }
                }

                if(t != r) fw = true;
            }
        }

        if(fw)
        {
            cout << "Case #" << it << ": Fegla Won" << endl;
            continue;
        }

        ans = 0;
        for(j = 0; j < rl; ++j)
        {
            sum = 0;
            for(i = 0; i < n; ++i) sum += d[i][j];
            sum /= n;
            for(i = 0; i < n; ++i) ans += abs(sum - d[i][j]);
        }

        cout << "Case #" << it << ": " << ans << endl;
    }

    return 0;
}
