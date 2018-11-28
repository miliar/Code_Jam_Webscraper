#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <algorithm>
#include <map>
#include <list>
#include <vector>
#include <queue>
#include <deque>
#include <sstream>
#include <fstream>
#include <ctime>
#include <numeric>
#include <functional>
#include <iterator>
using namespace std;

#define mp make_pair
#define pb push_back
#define all(c) ((c).begin(), (c).end())
#define sqr(a) ((a) * (a))
#define forn(i, n) for(int (i) = 0; (i) < (n); (i)++)
#define form(i, n) for(int (i) = 1; (i) <= (n); (i)++)
#define fab(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define fba(i, b, a) for(int (i) = (b); (i) >= (a); (i)--)

void SolveTheProblem()
{
    double c, f, x;
    cin >> c >> f >> x;
    double ans = x / 2.0, ps = 2.0, cur_sum = 0;
    for (int i = 0; i < 10000000; i++) {
        ans = min(ans, cur_sum + x / ps);
        cur_sum += c / ps;
        ps += f;
    }
    ans = min(ans, cur_sum + x / ps);

    cout.setf(ios::fixed);
    cout.precision(7);
    cout << ans << endl;
}

int main(void)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int n;
    cin >> n;
    form(t, n) {
        cout << "Case #" << t << ": ";
        SolveTheProblem();
    }
    return 0;
}