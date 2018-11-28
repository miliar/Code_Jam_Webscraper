#include <iostream>
#include <array>
#include <set>
#include <algorithm>
#include <cstdio>

using namespace std;

typedef std::array<std::array<int, 4>, 4> grid;

grid read()
{
    grid a;
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            cin >> a[i][j];
    return a;
}

int main(int argc, char **argv, char **envp)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T; cin >> T;

    for(int t = 0; t < T; ++t)
    {
        int ans1;cin >> ans1;
        grid g1 = read();

        int ans2;cin >> ans2;
        grid g2 = read();

        ans1--; ans2--;

        std::set<int> c1;
        for(int i = 0; i < 4; ++i)
            c1.insert(g1[ans1][i]);

        std::set<int> c2;
        for(int i = 0; i < 4; ++i)
            c2.insert(g2[ans2][i]);

        std::set<int> inter;

        std::set_intersection(c1.begin(), c1.end(), c2.begin(), c2.end(), std::inserter(inter, inter.begin()));

        if(inter.size() == 0)
            printf("Case #%d: Volunteer cheated!\n", t + 1);
        else if(inter.size() == 1)
            printf("Case #%d: %d\n", t + 1, *inter.begin());
        else
            printf("Case #%d: Bad magician!\n", t + 1);
    }

    return 0;
}