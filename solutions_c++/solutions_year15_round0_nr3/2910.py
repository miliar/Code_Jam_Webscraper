
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <map>


using namespace std;

struct p1 {
    char c;
    int sign;
};

p1 Calculate(map<pair<char, char>, p1> &table, p1 v1, char c)
{
    p1 res = table[make_pair(v1.c, c)];
    res = { res.c, v1.sign * res.sign };
    return res;
}

p1 Calculate1(map<pair<char, char>, p1> &table, char c, p1 v1)
{
    p1 res = table[make_pair(c, v1.c)];
    res = { res.c, v1.sign * res.sign };
    return res;
}


p1 GetValue(map<pair<char, char>, p1> &table, string &input, int s, int e)
{
    p1 cur = { input[s], 1};
    for (int i = s + 1; i <= e; i++)
    {
        p1 next = { input[i], 1 };
        p1 res = table[make_pair(cur.c, next.c)]; 

        cur = { res.c, cur.sign * res.sign };
    }
    return cur;
}

int main()
{
    int T;

    //ifstream fin("C:\\weilin\\Competition\\GCJ2015\\GCJ2015\\input.txt");
    ifstream fin("C:\\weilin\\Competition\\GCJ2015\\GCJ2015\\C-small-attempt1.in");
    ofstream fout("output.txt");

    fin >> T;
    int res = 0;
    long long total = 0;

    map<pair<char, char>, p1> table;
    table[make_pair('1', '1')] = { '1', 1 };

    table[make_pair('1', 'i')] = { 'i', 1 };

    table[make_pair('1', 'j')] = { 'j', 1 };

    table[make_pair('1', 'k')] = { 'k', 1 };

    table[make_pair('i', '1')] = { 'i', 1 };

    table[make_pair('i', 'i')] = { '1', -1 };

    table[make_pair('i', 'j')] = { 'k', 1 };

    table[make_pair('i', 'k')] = { 'j', -1 };

    table[make_pair('j', '1')] = { 'j', 1 };

    table[make_pair('j', 'i')] = { 'k', -1 };

    table[make_pair('j', 'j')] = { '1', -1 };

    table[make_pair('j', 'k')] = { 'i', 1 };

    table[make_pair('k', '1')] = { 'k', 1 };

    table[make_pair('k', 'i')] = { 'j', 1 };

    table[make_pair('k', 'j')] = { 'i', -1 };

    table[make_pair('k', 'k')] = { '1', -1 };



    for (int i = 0; i < T; i++)
    {
        int L, X;
        fin >> L >> X;
        string s;
        fin >> s;

        string input;
        for (int j = 0; j < X; j++)
        {
            input.append(s);
        }

        vector<p1> v;
        

        int len = L * X;

        v.assign(len, { '1', 1 });
        p1 res = { input[len - 1], 1 };
        v[len - 1] = res;

        for (int k = len - 2; k >= 0; k--)
        {
            res = Calculate1(table, input[k], res);
            v[k] = res;
        }



        bool possible = false;

        p1 cur = { input[0], 1 };

        for (int j = 0; j < len-2; j++)
        {
            if (j != 0)
            {
                cur = Calculate(table, cur, input[j]);
            }
            if (cur.c == 'i' && cur.sign == 1)
            {
                p1 cur1 = { input[j + 1], 1 };
                for (int k = j + 1; k < len-1; k++)
                {
                    if (k != j + 1)
                    {
                        cur1 = Calculate(table, cur1, input[k]);
                    }
                    if (cur1.c == 'j' && cur1.sign == 1)
                    {
                        p1 res = v[k + 1];
                        if (res.c == 'k' && res.sign == 1)
                        {
                            possible = true;
                            break;
                        }
                    }

                }

                if (possible == true)
                    break;

            }
        }

        if (possible)
        {
            fout << "Case #" << i + 1 << ": " << "YES" << endl;
        }
        else
        {
            fout << "Case #" << i + 1 << ": " << "NO" << endl;
        }

        v.clear();

    }
    return 0;
}