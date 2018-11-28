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
#define MAXN 11000
#define MAXX 800

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <long long> vll;

int tests;
int n, x;
int a[MAXN];
int d[MAXX], u[MAXN];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >>tests;
    forn (it , tests) {
        forn (i, MAXX) d[i] = 0;
        forn (i, MAXN) u[i] = 0;
        cin >> n >> x;
        forn (i, n) {
            cin >> a[i];
            d[a[i]]++;
        }
        sort(a, a + n);
        reverse(a, a + n);
        int res = 0;
        for (int i = 0; i < n; i++) {
            int w = a[i];
            if (!d[w]) continue;
            d[w]--;
            for (int i = x - w; i >= 0; i--) {
                if (d[i]) {
                    d[i]--;
                    break;
                }
            }
            res++;
        }
        cout << "Case #" << it + 1 << ": " << res << endl;
    }
    return 0;
}
