#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int M, N;
        cin >> M >> N;
        vector<string> S(M);
        for (int i = 0; i < M; ++i)
            cin >> S[i];
        vector<int> assignment(M, 0);
        int best = 0;
        int best_ways = 0;
        while (true)
        {
            vector<vector<string> > strs(N);
            for (int i = 0; i < M; ++i)
                strs[assignment[i]].push_back(S[i]);
            bool bad = false;
            for (int i = 0; i < N; ++i)
            {
                if (strs[i].empty())
                {
                    bad = true;
                    break;
                }
            }
            if (!bad)
            {
                int score = 0;
                for (int i = 0; i < N; ++i)
                {
                    vector<vector<int> > trie;
                    trie.push_back(vector<int>(26, -1));
                    for (auto it = strs[i].begin(); it != strs[i].end(); ++it)
                    {
                        const string& s = *it;
                        int v = 0;
                        for (auto itC = s.begin(); itC != s.end(); ++itC)
                        {
                            int c = (int)*itC - 'A';
                            if (trie[v][c] == -1)
                            {
                                trie[v][c] = (int)trie.size();
                                trie.push_back(vector<int>(26, -1));
                            }
                            v = trie[v][c];
                        }
                    }
                    score += (int)trie.size();
                }
                if (score > best)
                {
                    best = score;
                    best_ways = 1;
                }
                else if (score == best)
                    ++best_ways;
            }
            for (int i = M - 1; ; --i)
            {
                if (i < 0)
                    goto l_done;
                if (++assignment[i] < N)
                    break;
                assignment[i] = 0;
            }
        }
    l_done:
        cout << "Case #" << testcase << ": " << best << " " << best_ways << "\n";
    }
    return 0;
}
