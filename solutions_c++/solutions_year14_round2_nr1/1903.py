#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdint>

using namespace std;

string minify(string a, vector<int> &c)
{
    for (int i = 0; i < a.length(); i++)
    {
        c.push_back(1);

        for (int j = i; j < a.length() - 1 && a[j] == a[j + 1]; j++)
        {
            c.back()++;
        }
        a.erase(i, c.back() - 1);

    }
    
    return a;
}


int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        return 1;
    }
    char name[256];
    strcpy(name, argv[1]);

    ifstream fin(name);
    name[strlen(name)-2] = 0;
    strcat(name, "out");
    ofstream fout(name);

    if (!fin.is_open() || !fout.is_open())
    {
        return 1;
    }

    int t, t1 = 0;

    fin >> t;

    while (t1++ < t)
    {
        int n;
        fin >> n;
        vector<string> s;
        s.resize(n);
        for (int i = 0; i < n; i++)
        {
            fin >> s[i];
        }
        vector<int> c[n];
        string m = minify(s[0], c[0]);
        bool is_fail = false;
        for (int i = 1; i < n; i++)
        {
            if (m != minify(s[i], c[i]))
            {
                is_fail = true;
                break;
            }
        }
        int move_count = 0;
        if (!is_fail)
        {
            int base[m.length()];
            for (int i = 0; i < m.length(); i++)
            {
                int sum = 0;
                for (int j = 0; j < n; j++)
                {
                    sum += c[j][i];
                }
                int mean = (int)(sum / (double)n + 0.5);
                sum = 0;
                for (int j = 0; j < n; j++)
                {
                    sum += abs(c[j][i] - mean);
                }
                move_count += sum;
            }
        }

        fout << "Case #" << t1 << ": ";
        if (is_fail)
        {
            fout << "Fegla Won" << endl;
        }
        else
        {
            fout << move_count << endl;
        }

    }

    return 0;
}