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
    int a[4];
    int b[4];
    int n;
    cin >> n;
    for (int i = 0; i < 4; i++) {
        int t;
        for (int j = 0; j < 4; j++) {
            cin >> t;
            if (i == n - 1) {
                a[j] = t;
            }
        }
    }
    cin >> n;
    for (int i = 0; i < 4; i++) {
        int t;
        for (int j = 0; j < 4; j++) {
            cin >> t;
            if (i == n - 1) {
                b[j] = t;
            }
        }
    }
    sort(a, a + 4);
    sort(b, b + 4);
    auto it = set_intersection(a, a + 4, b, b + 4, a);
    if (it - a == 0) {
        cout << "Volunteer cheated!" << endl;
        return;
    }
    if (it - a == 1) {
        cout << a[0] << endl;
        return;
    }
    cout << "Bad magician!" << endl;
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