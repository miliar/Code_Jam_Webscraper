#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define FOREACH(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define MOD 1000000007
#define INF 2000000000

int T, N, L;

string word;
vector<string> vg;
string b;

int main() {
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        printf("Case #%d: ", tc);
        vg = vector<string>();

        cin >> N >> L;

        FORN(i, N) {
            cin >> word;
            vg.PB(word);
        }

        cin >> b;

        bool ok = true;
        FORN(i, N) if (vg[i] == b) { cout << "IMPOSSIBLE\n"; ok = false; break; }

        if (ok) {
            cout << "0"; FORN(i, L-1) cout << "?"; cout << " ";
            cout << "10?"; FORN(i, 60) cout << "10"; cout << endl;
        }
    }
    
    return 0;
}
