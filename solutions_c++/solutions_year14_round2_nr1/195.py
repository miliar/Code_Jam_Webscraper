#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A.out");

vector<char> L[105];
vector<int> A[105];

int N, T;

int main()
{
    fin >> T;

    for(int t = 1; t <= T; t++)
    {
        fin >> N;

        for(int i = 0; i < 105; i++)
        {
            A[i].clear();
            L[i].clear();
        }

        for(int i = 0; i < N; i++)
        {
            string s;
            fin >> s;

            s += '.';

            char curr = s[0];
            int am = 1;

            for(int p = 1; p < s.length(); p++)
                if(s[p] != s[p-1])
                {
                    L[i].push_back(curr);
                    A[i].push_back(am);
                    curr = s[p];
                    am = 1;
                }
                else
                    am++;
        }

        bool poss = true;

        for(int i = 0; i < N; i++)
            for(int j = i+1; j < N; j++)
                if(L[i] != L[j])
                    poss = false;

        if(!poss)
        {
            fout << "Case #" << t << ": Fegla Won\n";
            continue;
        }

        int ans = 0;

        for(int l = 0; l < L[0].size(); l++)
        {
            int best = 999999;

            for(int k = 0; k <= 100; k++)
            {
                int cost = 0;

                for(int i = 0; i < N; i++)
                    cost += abs(k - A[i][l]);

                best = min(best,cost);
            }

            ans += best;
        }

        fout << "Case #" << t << ": " << ans << "\n";
    }
}
