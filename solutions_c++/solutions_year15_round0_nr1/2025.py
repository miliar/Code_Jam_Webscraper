#include <iostream>
#include <string>

using namespace std;

int main()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int nbT;
    cin >> nbT;
    for (int t = 1; t <= nbT; t++)
    {
        cout << "Case #" << t << ": ";
        int ans = 0;
        int curDebout = 0;
        int nbLvl;
        cin >> nbLvl;
        string nbParLvl;
        cin >> nbParLvl;

        for (int i = 0; i <= nbLvl; i++)
        {
            int curLvl = nbParLvl[i]-'0';
            if (curDebout < i)
            {
                ans += i-curDebout;
                curDebout = i;
            }
            curDebout += curLvl;
        }

        cout << ans << '\n';


    }
    return 0;
}
