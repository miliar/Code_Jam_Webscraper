#include <iostream>
#include <string>
#include <set>
#include <utility>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

int main()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    /*ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);*/

    int nbT;
    cin >> nbT;


    for (int t = 1; t <= nbT; t++)
    {
        int nbInter;
        cin >> nbInter;
        int nbWithTime[100000];

        int ans1 = 0, ans2 = 0;

        for (int j  =0; j < nbInter; j++)
        {
            int cur;
            cin >> cur;
            nbWithTime[j] = cur;
        }


        int maxRate = 0;
        for (int j = 0; j < nbInter-1; j++)
        {
            maxRate = max(maxRate, nbWithTime[j] - nbWithTime[j+1]);
            if (nbWithTime[j] >= nbWithTime[j+1])
            {

                ans1 += nbWithTime[j] - nbWithTime[j+1];
                //cout << j << endl;
            }
        }

        int nbCur = 0;
        //cout << "aaa" << maxRate << endl;
        for (int j = 0; j < nbInter-1; j++)
        {
            nbCur=nbWithTime[j];
           // cout << nbCur << "=>" << min(maxRate, nbCur) << endl;
            ans2 += min(maxRate, nbCur);

        }


        cout << "Case #" << t << ": " << ans1 << ' ' << ans2 << '\n';



    }
    return 0;
}
