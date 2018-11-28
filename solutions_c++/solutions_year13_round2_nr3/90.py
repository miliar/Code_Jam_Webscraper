#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

vector<string> dict;

string ss;

unsigned int dp[4000][5];

pair<int,int> matches(int idx, int wor, int m)
// check that dict[wor] is an "almost" prefix of ss[idx:] where the first difference happens after m chars
{
    int n = dict[wor].length();

    if (n > ss.length() - idx)
    {
        return make_pair(-1, -1);
    }

    int res = 0;
    for (int i = 0; i < n; i += 1)
    {
        if (ss[idx+i] != dict[wor][i])
        {
            if (i < m)
            {
                return make_pair(-1, -1);
            }
            else
            {
                res += 1;
                m = i + 5;  // XXX 5 or 4?
            }
        }
    }
    
    return make_pair(res, max(0, m - n));
}

int elabora ()
{
    cin >> ss;

    int n = ss.length();

    for (int j = 0; j < 5; j += 1)
    {
        dp[0][j] = 0;
    }
    for (int i = 1; i < n; i += 1)
    {
        for (int j = 0; j < 5; j += 1)
        {
            dp[i][j] = 4000000000;
        }
    }

    unsigned int res = 4000000000;
    for (int i = 0; i < n; i += 1)
    {
        for (int j = 0; j < 5; j += 1)
        {
            if (dp[i][j] >= 4000000000)
            {
                continue;
            }

            for (int k = 0; k < dict.size(); k += 1)
            {
                pair<int,int> r = matches(i, k, j);
                if (r.first != -1)
                {
                    int i1 = i + dict[k].length();
                    if (i1 >= n)
                    {
                        if (dp[i][j] + r.first < res)
                        {
                            res = dp[i][j] + r.first;
                            // cout << "+++ res updated to " << res << " thanks to " << dict[k] << " on " << i << " with " << j << endl;
                        }
                    }
                    else
                    {
                        if (dp[i][j] + r.first < dp[i1][r.second])
                        {
                            dp[i1][r.second] = dp[i][j] + r.first;
                            // cout << " +  dp[" << i1 << "][" << r.second << "] updated to " << dp[i1][r.second] << " thanks to " << dict[k] << " on " << i << " with " << j << endl;
                        }
                    }
                }
            }
        }
    }

    return res;
}

int main ()
{
    ifstream d("garbled_email_dictionary.txt");
    for (int i = 0; i < 521196; i += 1)
    {
        string s;
        d >> s;
        dict.push_back(s);
    }

    int tcs;
    cin >> tcs;
    for (int i = 1; i <= tcs; i += 1)
    {
        unsigned int res = elabora();
        cout << "Case #" << i << ": " << res << endl;
    }
}
