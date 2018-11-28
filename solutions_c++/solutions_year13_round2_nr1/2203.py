#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>

using namespace std;

struct GCase
{
    int A;
    int N;
    vector<int> motes;
    int solve()
    {
        sort(motes.begin(), motes.end());
        return solveRecursive(A, motes.begin());
    }
    int solveRecursive(int a, vector<int>::iterator iter)
    {
        //return solveRecursive(a, iter);
        if (iter == motes.end())
            return 0;
        if (a <= *iter)
        {
            if (a != 1)
            {
                int c0 = solveRecursive(2*a-1, iter); // add
                ++iter;
                int c1 = solveRecursive(a, iter); // delete
                return (c0 < c1? c0: c1) + 1;
            }
            else
                return solveRecursive(a, ++iter) + 1; // delete
        }
        else
        {
            int tmp = *iter;
            return solveRecursive(a + tmp, ++iter);
        }
        return 0;
    }
};

int g_nCases = 0;
vector<GCase*> g_cases;

void read_input()
{
    cin >> g_nCases;
    for (int i = 0; i < g_nCases; ++i)
    {
        GCase* gc = new GCase;
        // do sth
        cin >> gc->A >> gc->N;
        int m;
        for (int i = 0; i < gc->N; ++i)
        {
            cin >> m;
            gc->motes.push_back(m);
        }
        g_cases.push_back(gc);
    }
}

int main(int argc, char**argv)
{
    read_input();

    for (int i = 0; i < g_nCases; ++i)
    {
        cout << "Case #" << i+1 << ": " << g_cases[i]->solve();
        cout << endl;
    }
    return 0;
}
