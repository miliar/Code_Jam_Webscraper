#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

const int maxans = 1e3;
const int maxn = 1e3 + 10;
const int oo = 1e6;

typedef pair <int, int> pt;

int a[maxn];

int main()
{
    ifstream cin ("prob2.inp");
    ofstream cout ("prob2.out.1");
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++)
    {
        cout << "Case #" << tt << ": ";
        int d;
        cin >> d;
        int maxa = 0;
        for (int i = 1; i <= d; i++)
        {
            cin >> a[i];
            maxa = max(maxa, a[i]);
        }
        int res = oo;
        for (int ans = 1; ans <= maxa; ans++)
        {

            int tmp = ans;
            for (int i = 1; i <= d; i++)
            {
                if (a[i] > ans)
                {
                    tmp += (a[i] - ans) / ans;
                    if (a[i] % ans)
                        tmp++;
                }
            }
            res = min(res, tmp);
        }
        cout << res << "\n";
    }
}
