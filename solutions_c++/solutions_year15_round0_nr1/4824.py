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
const int MAXN = 1000;
int nTest, n, sum[MAXN + 9], ans;
char a[MAXN + 9];

int main()
{
    ifstream cin("a.inp");
    ofstream cout("a.out");
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> nTest;
    for(int iTest = 1; iTest <= nTest; iTest++)
    {
        cin >> n;
        for(int i = 0; i <= n; i++)
        {
            cin >> a[i];
        }
        ans = 0;
        sum[0] = a[0] - '0';
        for(int i = 1; i <= n; i++)
        {
            sum[i] = sum[i - 1] + a[i] - '0';
        }
        for(int i = 1; i <= n; i++)
        {
            ans = max(ans, i - sum[i - 1]);
        }
        cout << "Case #" << iTest << ": " << ans << "\n";
    }
    return 0;
}
