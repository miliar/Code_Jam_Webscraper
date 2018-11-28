#include <fstream>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

ifstream fin("C-small.in");
ofstream fout("C.out");

bool E[55][55], Ret[55][55], V[55];
int N, M, T, Total;
set<string> Set;
string Codes;
vector<string> Zip(55,"");

void dfs(int n)
{
    if(!Set.empty() && Codes > *Set.begin())
        return;

    if(Total == 2*N)
    {
        Set.insert(Codes);
        return;
    }

    for(int i = 0; i <= N; i++)
        if(Ret[n][i])
        {
            if(i == 0 && Total < 2*N-1)
                continue;

            Ret[n][i] = false;

            Total++;
            dfs(i);
            Total--;

            Ret[n][i] = true;
        }

    for(int i = 1; i <= N; i++)
        if(!V[i] && E[n][i])
        {
            V[i] = true;
            Ret[i][n] = true;

            string prev = Codes;
            Codes += Zip[i];

            Total++;
            dfs(i);
            Total--;

            Codes = prev;

            Ret[i][n] = false;
            V[i] = false;
        }
}

int main()
{
    fin >> T;

    for(int t = 1; t <= T; t++)
    {
        cout << t << "\n";
        fin >> N >> M;

        Set.clear();

        for(int i = 0; i < 55; i++)
            for(int j = 0; j < 55; j++)
                E[i][j] = false;

        for(int i = 1; i <= N; i++)
        {
            fin >> Zip[i];
            E[0][i] = true;
        }

        for(int i = 0; i < M; i++)
        {
            int a, b;
            fin >> a >> b;
            E[a][b] = E[b][a] = true;
        }

        dfs(0);

        fout << "Case #" << t << ": " << *Set.begin() << "\n";
    }
}
