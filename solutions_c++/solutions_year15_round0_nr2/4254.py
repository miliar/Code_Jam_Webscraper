#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <complex>
#include <locale>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
using namespace std;
const int MAXN = 1000, MAXA = 1000;
int nTest, n, a[MAXN + 9], ans;

int main()
{
    ifstream cin("b.inp");
    ofstream cout("b.out");
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> nTest;
    for(int iTest = 1; iTest <= nTest; iTest++)
    {
        cin >> n;
        for(int i = 1; i <= n; i++)
        {
            cin >> a[i];
        }
        ans = MAXA;
        for(int lvl = 1; lvl <= MAXA; lvl++)
        {
            int sum = lvl;
            for(int i = 1; i <= n; i++)
            {
                sum += (a[i] - 1) / lvl;
            }
            ans = min(ans, sum);
        }
        cout << "Case #" << iTest << ": " << ans << "\n";
    }
    return 0;
}
