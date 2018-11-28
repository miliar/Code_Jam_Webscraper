#include <iostream>
#include <cfloat>
#include <iomanip>
using namespace std;
void solve(int caseId)
{
    long double c, f,x;
    cin >> c >> f >> x;
    long double ans = LDBL_MAX;
    long double rate = 2.0;
    long double time = 0.0;
    do
    {
        ans = min(time + x / rate , ans);
        time += c / rate;
        rate += f;
    } while (time < ans);
    cout << "Case #" << caseId << ": " << fixed << setprecision(9) << ans << endl;
}
int main()
{
    int t;
    cin >> t;
    for (int i = 0 ; i < t; ++i)
        solve(i + 1);
    return 0;
}
