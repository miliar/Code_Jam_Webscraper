#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

map<string, int> M;

int dfs(vector<int> vi)
{
    if (vi.size() == 0)
        return 0;

    int res = 1000;
    string m = "";
    sort(vi.begin(), vi.end());
    for (vector<int>::iterator it = vi.begin(); it != vi.end(); it++)
        m += (char)(*it + '0');
    if (M.find(m) != M.end())
        return M[m];

    vector<int> way;
    for (int i = 0; i < vi.size(); i++) if (vi[i]) way.push_back(vi[i] - 1);
    res = min(res, 1 + dfs(way));

    for (int i = 0; i < vi.size(); i++)
    {
        int cur = vi[i];
        if (cur > 1)
        {
            for (int j = 1; j <= cur / 2; j++)
            {
                vector<int> tmp = vi;
                tmp[i] = j;
                tmp.push_back(cur - j);
                res = min(res, 1 + dfs(tmp));
            }
        }
    }

    return M[m] = res;
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++)
    {
        int D, P;
        scanf("%d", &D);
        vector<int> cakes;
        for (int i = 0; i < D; i++)
        {
            scanf("%d", &P);
            cakes.push_back(P);
        }

        printf("Case #%d: %d\n", c, dfs(cakes));
    }
}