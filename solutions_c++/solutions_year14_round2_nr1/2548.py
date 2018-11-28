#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
#define MAXT 120
#define MAXN 120

using namespace std;

vector<pair<char, int>> chs[MAXN];

int main()
{
    ifstream fin("A-small-attempt01.in");
    ofstream fout("A-small-attempt0.out");
    int t, n;
    bool lost;
    string s;
    int cnt, sum, avg, sol;

    fin >> t;
    for (int a = 1; a <= t; a++)
    {
        for (int i = 0; i < MAXN; i++)
        {
            chs[i].erase(chs[i].begin(), chs[i].end());
        }

        fin >> n;
        for (int i = 0; i < n; i++)
        {
            fin >> s;
            cnt = 1;
            for (int j = 0; j < s.size(); j++)
            {
                if (s[j] == s[j+1])
                {
                    cnt++;
                }
                else
                {
                    chs[i].push_back(make_pair(s[j], cnt));
                    cnt = 1;
                }
            }
        }

        lost = false;
        for (int i = 1; i < n; i++)
        {
            if (chs[i-1].size() != chs[i].size())
            {
                lost = true;
                break;
            }
        }

        if (lost)
        {
            fout << "Case #" << a << ": Fegla Won" << endl;
            continue;
        }

        sol = 0;
        for (int i = 0; i < chs[0].size(); i++)
        {
            sum = chs[0][i].second;
            for (int j = 1; j < n; j++)
            {
                if (chs[j-1][i].first == chs[j][i].first)
                {
                    sum += chs[j][i].second;
                }
                else
                {
                    lost = true;
                    break;
                }
            }

            if (lost)
            {
                break;
            }

            avg = round(1.0 * sum / n);

            for (int j = 0; j < n; j++)
            {

                sol += abs(avg - chs[j][i].second);

            }
        }

        if (lost)
        {
            fout << "Case #" << a << ": Fegla Won" << endl;
            continue;
        }
        else
        {
            fout << "Case #" << a << ": " << sol << endl;
        }

    }


    return 0;
}
