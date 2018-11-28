#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

vector<pair<int, pair<string, string>>> mozliwosci; // roznica, c, j
int minimum;

void Szukaj(string c, string j)
{
    bool zm = false;
    string pom;
    for(int i = 0; i < c.length(); ++i)
    {
        if (c[i] == '?')
        {
            zm = true;
            pom = c;
            for (auto x : {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
            {
                pom[i] = x;
                Szukaj(pom, j);
            }
        }
    }
    if (!zm)
    {
        for(int i = 0; i < j.length(); ++i)
        {
            if (j[i] == '?')
            {
                zm = true;
                pom = j;
                for (auto x : {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
                {
                    pom[i] = x;
                    Szukaj(c, pom);
                }
            }
        }
    }
    if (!zm)
    {
        if (abs(stoi(c) - stoi(j)) <= minimum)
        {
            mozliwosci.push_back(make_pair(abs(stoi(c) - stoi(j)), make_pair(c, j)));
            minimum = min(minimum, abs(stoi(c) - stoi(j)));
        }
    }
}

int main()
{
    int T;
    cin >> T;


    string c, j;

    for (int t = 1; t <= T; ++t)
    {
        cin >> c >> j;
        //cout << c << j << endl;
        minimum = 100000000000;
        Szukaj(c, j);
        sort(mozliwosci.begin(), mozliwosci.end());
        cout << "Case #" << t << ": " << mozliwosci[0].second.first << " " << mozliwosci[0].second.second << endl;
        mozliwosci.clear();
    }


    return 0;
}
