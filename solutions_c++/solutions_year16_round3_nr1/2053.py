#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

ifstream fin("senate.in");
ofstream fout("senate.out");


bool operator < (pair<int, char> p1, pair<int, char> p2)
{
    return p1.first < p2.first;
}

int main(int argc, char const *argv[])
{
    char alpha[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    int t;
    fin >> t;
    for (int x = 0; x < t; ++x)
    {
        fout << "Case #" << x + 1 << ": ";
        priority_queue<pair<int, char>> plan;
        int senators = 0;
        int n;
        fin >> n;
        for (int i = 0; i < n; ++i)
        {
            int q;
            fin >> q;
            senators += q;
            char p = alpha[i];
            plan.push({q, p});
        }

        while (!plan.empty())
        {
            pair<int, char> top = plan.top();
            plan.pop();
            senators--;
            fout << top.second;
            if (--top.first != 0)
            {
                plan.push(top);
            }
            top = plan.top();
            if (top.first > senators/2)
            {
                plan.pop();
                senators--;
                fout << top.second;
                if (--top.first != 0)
                {
                    plan.push(top);
                }
            }
            fout << " ";
        }
        fout << endl;
    }


    return 0;
}