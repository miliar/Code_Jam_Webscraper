#include <iostream>
#include <fstream>
#include <set>
#include <cstdlib>
#include <array>

using namespace std;

int main()
{
    ofstream cout("output.txt");
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int q;
    array<array<int, 4>, 4> V;
    cin >> q;
    for (int num = 1; q; q--, num++)
    {
        cout << "Case #" << num << ": ";
        int n;
        cin >> n;
        set<int> a, b, ans;
        for (auto i = 0; i < V.size(); i++)
            for (auto j = 0; j < V[i].size(); j++)
                cin >> V[i][j];
        for (auto i = 0; i < V.size(); i++)
            a.insert(V[n - 1][i]);
        cin >> n;
        for (auto i = 0; i < V.size(); i++)
            for (auto j = 0; j < V[i].size(); j++)
                cin >> V[i][j];
        for (auto i = 0; i < V.size(); i++)
            b.insert(V[n - 1][i]);
        for (auto i : a)
            if (b.count(i))
                ans.insert(i);
        if (ans.size() == 0)
            cout << "Volunteer cheated!\n";
        else if (ans.size() > 1)
            cout << "Bad magician!\n";
        else
            cout << *ans.begin() << '\n';
    }
    return 0;
}
