#include <bits\stdc++.h>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
//   {{{"1", '1'}, "1"},   {{"1", '2'}, "2"},   {{"1", '3'}, "3"},   {{"1", '4'}, "4"},
//    {{"2", '1'}, "2"},   {{"2", '2'}, "-1"},  {{"2", '3'}, "4"},   {{"2", '4'}, "-3"},
//    {{"3", '1'}, "3"},   {{"3", '2'}, "-4"},  {{"3", '3'}, "-1"},  {{"3", '4'}, "2"},
//    {{"4", '1'}, "4"},   {{"4", '2'}, "3"},   {{"4", '3'}, "-2"},  {{"4", '4'}, "-1"},
//    {{"-1", '1'}, "-1"}, {{"-1", '2'}, "-2"}, {{"-1", '3'}, "-3"}, {{"-1", '4'}, "-4"},
//    {{"-2", '1'}, "-2"}, {{"-2", '2'}, "1"},  {{"-2", '3'}, "-4"}, {{"-2", '4'}, "3"},
//    {{"-3", '1'}, "-3"}, {{"-3", '2'}, "4"},  {{"-3", '3'}, "1"},  {{"-3", '4'}, "-2"},
//    {{"-4", '1'}, "-4"}, {{"-4", '2'}, "-3"}, {{"-4", '3'}, "2"},  {{"-4", '4'}, "1"}};
    vector<vector<int>> M = {{0, -4, -3,  2,  1},
                             {0, -3,  4,  1, -2},
                             {0, -2,  1, -4,  3},
                             {0, -1, -2, -3, -4},
                             {0,  0,  0,  0,  0},
                             {0,  1,  2,  3,  4},
                             {0,  2, -1,  4, -3},
                             {0,  3, -4, -1,  2},
                             {0,  4,  3, -2, -1}};
    int TESTS;
    cin >> TESTS;
    for (int TEST = 1; TEST <= TESTS; TEST++)
    {
        cerr << TEST << '\n';
        int l, x;
        string SS, S;
        cin >> l >> x >> SS;
        cout << "Case #" << TEST << ": ";
        while (x --> 0)
            S += SS;
        vector<vector<int>> J(S.size());
        set<int> K;
        for (size_t i = 1; i < S.size(); i++)
        {
            int sec = S[i] - 'i' + 2;
            size_t j = i + 1;
            while (j < S.size())
            {
                if (sec == 3)
                    J[i].push_back(j);
                sec = M[sec + 4][S[j++] - 'i' + 2];
            }
            if (sec == 4)
                K.insert(i);
        }
        int fir = 1;
        for (size_t i = 0; i + 2 < S.size(); i++)
        {
            fir = M[fir + 4][S[i] - 'i' + 2];
            if (fir == 2)
            {
                for (auto & x : J[i + 1])
                    if (K.count(x))
                    {
                        cout << "YES\n";
                        goto label1;
                    }
            }
        }
        cout << "NO\n";
label1:;
    }
}
