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
#define MAXN 20

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <long long> vll;


int t;
int a[4][4];
int u[MAXN];
int x;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    forn (it, t) {
        forn (i, MAXN) u[i] = 0;

        cin >> x;
        forn (i, 4) forn (j, 4) cin >> a[i][j];
        x--;
        forn (j, 4) u[a[x][j]]++;

        cin >> x;
        forn (i, 4) forn (j, 4) cin >> a[i][j];
        x--;
        forn (j, 4) u[a[x][j]]++;
        int t = 0, ans = 0;
        forn (i, MAXN) {
            if (u[i] == 2) {
                t++;
                ans = i;
            }
        }
        printf("Case #%d: ", it + 1);
        if (t == 1) {
            cout << ans << endl;
        }
        if (t == 0) {
            cout << "Volunteer cheated!\n";
        }
        if (t > 1) {
            cout << "Bad magician!\n";
        }
    }
    return 0;
}
