#include <fstream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>
using namespace std;

int main()
{
    int N, T, i, j, k, x, length;
    ifstream f("input.in");
    ofstream g("output.out");

    f >> T;
    for (i = 1; i <= T; i++)
    {
        f >> N;
        g << "Case #" << i << ": ";
        length = 2 * N - 1;
        unordered_map<int, int> missing;
        for (j = 0; j < length; j++)
        {
            for (k = 0; k < N; k++)
            {
                f >> x;
                missing[x]++;

            }
        }

        vector<int> sol;
        for (auto it = missing.begin(); it != missing.end(); it++)
            if (it->second % 2 != 0)
                sol.push_back(it->first);
        sort(sol.begin(), sol.end());
        for (j = 0; j < sol.size(); j++)
            g << sol[j] << ' ';
        g << '\n';
    }


    f.close();
    g.close();
    return 0;
}
