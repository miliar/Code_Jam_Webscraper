#include <iostream>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <vector>

#define ull unsigned long long
#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define iter iterator

using namespace std;

void Solve()
{
    cout.precision(20);

    long double c, f, x;
    cin >> c >> f >> x;
    long double sum = 0;
    long int cnt = 0;
    while ((x - c) / (2 + cnt * f) > (x) / (2 + (cnt + 1)*f))
    {
        sum += c / (2 + cnt * f);
        ++cnt;
    }
    sum +=  x / (2 + cnt * f);
    cout << sum;
}

int main()
{
    freopen("test.txt", "r", stdin);
    freopen("ans.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    int NumOfTests;
    cin >> NumOfTests;
    for (int i = 1; i <= NumOfTests; ++i)
    {
        cout << "Case #" << i << ": ";
        Solve();
        cout << endl;
    }
}
