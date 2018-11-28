#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
#include <set>
#include <string>

using namespace std;


int main(void)
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    freopen("t.in", "r", stdin);
    //freopen("t.out", "w", stdout);


    int nbT;
    cin >> nbT;



    for (int t = 1; t <= nbT; t++)
    {
        string s;
        cin >> s;

        string rep;
        rep = rep+s[0];

        for (int i = 1; i < s.size(); i++)
        {
            if (s[i] >= rep[0])
                rep   = s[i]+rep;
            else
                rep.push_back(s[i]);
        }


        cout << "Case #" << t << ": " << rep << '\n';
    }


    return 0;
}
