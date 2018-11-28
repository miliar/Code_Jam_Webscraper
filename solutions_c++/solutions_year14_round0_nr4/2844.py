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
    int n;
    cin >> n;
    vector <double> kn(n), nm(n);
    int u[10001];
    memset(u, 0, sizeof(u));
    forn(i, n) {
        cin >> nm[i];
    }
    forn(i, n) {
        cin >> kn[i];
    }
    sort(kn.begin(), kn.end());
    sort(nm.begin(), nm.end());
    int z = 0;
    forn(i, n) {
        int j = 0;
        while (j < n && (u[j] == 1 || kn[j] < nm[i])) {
            ++j;
        }
        if (j < n) {
            u[j] = 1;
        }
        else {
            j = 0;
            while (j < n && u[j] == 1) {
                ++j;
            }
            u[j] = 1;
            ++z;
        }
    }
    int y = 0, fst = 0, lst = n - 1;
    forn(i, n) {
        if (nm[i] > kn[fst]) {
            ++y;
            ++fst;
        }
        else {
            --lst;
        }
    }
    cout << y << ' ' << z << endl;
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