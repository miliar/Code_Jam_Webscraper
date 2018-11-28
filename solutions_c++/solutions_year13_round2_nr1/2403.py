#include <iostream>
#include <set>
#include <vector>
#include <cstdlib>
using namespace std;

bool finish = false;

void Print(vector <int> V)
{
    for (int i = 0; i < V.size(); ++i)
        cout << V[i] << " ";
    cout << endl;
}

bool Check(vector <int> V, multiset <int> M, int S)
{
    if (M.empty())
        return true;
    for (int i = 0; i < V.size() - 1; ++i)
    {
        if (V[i] == 1)
            S = 2 * S - 1;
        else
            M.erase(--M.end());
        while (!M.empty() && (*M.begin()) < S)
        {
            S += (*M.begin());
            M.erase(M.begin());
        }
        if (M.empty())
            return true;
    }
    return false;
}

void Gen(vector <int> & V, multiset <int> & M, int & S, long unsigned int & Max, int n)
{
    if (n <= M.size())
    {
        V.push_back(0);
        if (Check(V, M, S))
            Max = min(Max, V.size() - 1);
        V.pop_back();
        V.push_back(1);
        if (Check(V, M, S))
            Max = min(Max, V.size() - 1);
        V.pop_back();
        if (!finish)
        {
            V.push_back(0);
            Gen(V, M, S, Max, n + 1);
            V.pop_back();
            V.push_back(1);
            Gen(V, M, S, Max, n + 1);
            V.pop_back();
        }
    }
}

void Solve()
{
    finish = false;
    int A, N, CurS, cnt = 0, s;
    cin >> A >> N;
    CurS = A;
    multiset <int> Motes;
    for (int i = 0; i < N; ++i)
    {
        cin >> s;
        Motes.insert(s);
    }
    set <int>::iterator it = Motes.begin();
    while (!Motes.empty() && (*Motes.begin()) < CurS)
    {
        CurS += (*Motes.begin());
        Motes.erase(Motes.begin());
    }
    vector <int> V;
    long unsigned int Max = 100000000;
    Gen(V, Motes, CurS, Max, 0);
    cout << Max << endl;
}

int main()
{
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
