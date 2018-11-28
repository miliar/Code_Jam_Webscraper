#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <climits>

using namespace std;

#define FOR(k,a,b) for(int k=(a); k < (b); k++)
#define FORE(k,a,b) for(int k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define ALL(c) (c).begin(), (c).end()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define RANGE(lb, x, ub) ((lb) <= (x) && (x) < (ub))

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-10;


int main()
{
    int T; cin >> T;
    REP(tcase, T) {
        int X, R, C; cin >> X >> R >> C;
        string winner;

        if(X == 1) {
            winner = "GABRIEL";
        }
        else if(X == 2) {
            if((R * C) % 2 == 0) winner = "GABRIEL";
            else winner = "RICHARD";
        }
        else if(X == 3) {
            winner = "RICHARD";
            if(((R >= 3) && (C >= 2)) || ((R >= 2) && (C >= 3))) {
                if((R * C) % 3 == 0)
                    winner = "GABRIEL";
            }
        }
        else if(X == 4) {
            winner = "RICHARD";
            if((R * C == 12) || (R * C) == 16) {
                winner = "GABRIEL";
            }
        }

        printf("Case #%d: ", tcase + 1);
        //printf("%d %d %d ", X, R, C);
        cout << winner << endl;
    }


    return 0;
}
