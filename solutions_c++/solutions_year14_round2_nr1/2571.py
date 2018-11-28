#include <iostream>
#include <string>
#include <vector>

using namespace std;

int T;
int N;

struct Elem
{
    char c;
    int count;
};

vector<string> strings;
vector<vector<Elem>> elemVec;

vector<Elem> Convert(const string & s)
{
    Elem e;
    e.c = s[0];
    e.count = 0;
    vector<Elem> elems;
    for (size_t i = 0; i < s.size(); ++i)
    {
        if (s[i] == e.c)
        {
            ++e.count;
        }
        else
        {
            elems.push_back(e);
            e.c = s[i];
            e.count = 1;
        }
    }
    elems.push_back(e);
    return elems;
}

void Solve(int t)
{
    elemVec.resize(N);
    for (int i = 0; i < N; ++i)
    {
        elemVec[i] = Convert(strings[i]);
    }

    bool impossible = false;
    for (size_t i = 0; i < elemVec.size(); ++i)
    {
        if (elemVec[i].size() != elemVec[0].size())
        {
            impossible = true;
            break;
        }
    }

    if (!impossible)
    {
        int total = 0;
        for (size_t i = 0; i < elemVec[0].size(); ++i)
        {
            int minCount = 1000;
            char c = elemVec[0][i].c;
            for (int j = 1; j <= 100; ++j)
            {
                int count = 0;
                for (size_t k = 0; k < elemVec.size(); ++k)
                {
                    if (elemVec[k][i].c != c)
                    {
                        cout << "Case #" << t << ": Fegla Won" << endl;
                        return;
                    }
                    else
                    {
                        count += abs(elemVec[k][i].count - j);
                    }
                }
                if (count < minCount)
                {
                    minCount = count;
                }
            }
            total += minCount;
        }
        cout << "Case #" << t << ": " << total << endl;
    }
    else
    {
        cout << "Case #" << t << ": Fegla Won" << endl;
    }
}

int main()
{
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> N;
        strings.resize(N);
        for (int i = 0; i < N; ++i)
        {
            cin >> strings[i];
        }
        Solve(t);
    }
    int a = 0;
}
