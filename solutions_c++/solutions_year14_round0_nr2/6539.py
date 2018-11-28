#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define INF 2e9
#define pb push_back
#define mp make_pair
#define forn(i,n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <long long> vll;

int t;
double c, f, x;
const int MAX = 200000;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    cout.precision(10);
    forn (it, t) {
        cin >> c >> f >> x;
        double ans = INF;
        double res1 = 0, speed = 2., res;
        for (int k = 0; k < MAX; k++) {
            res = x / speed + res1;
            ans = min(ans, res);
            res1 += c / speed;
            speed += f;
        }
        cout << "Case #" << it + 1 << ": ";

        cout << ans << endl;
    }
    return 0;
}
