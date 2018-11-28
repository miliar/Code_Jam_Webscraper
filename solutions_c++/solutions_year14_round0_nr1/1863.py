#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <utility>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define F first
#define S second
#define PB push_back
#define MP make_pair

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = 2123123123;
const int MOD = 1e9+7;

typedef long long ll;
typedef pair<int,int> pii;

#define ALL(c) (c).begin(), (c).end()
#define SZ(a) (int)(a).size()
#define RESET(a,x) memset(a,x,sizeof(a))
#define FORIT(it,v) for(__typeof(v.begin()) it = v.begin(); it != v.end(); ++it)
#define MX(a,b) a = max((a),(b));
#define MN(a,b) a = min((a),(b));

inline void OPEN(const string &s) {
	freopen((s + ".in").c_str(), "r", stdin);
	freopen((s + ".out").c_str(), "w", stdout);
}

int ntc, carol;
int vis[17];
int cacha[4][4];

int main() {
    OPEN("A");
    scanf("%d", &ntc);
    for (int itc = 0; itc < ntc; itc++) {
        RESET(vis,0);
        int take = 0, p;
        vector<int> anita;
        scanf("%d", &p);
        printf("Case #%d: ", itc+1);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                scanf("%d", &cacha[i][j]);
                if (i+1 == p) anita.PB(cacha[i][j]);
            }
        scanf("%d", &p);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                scanf("%d", &cacha[i][j]);
                if (i+1 == p) anita.PB(cacha[i][j]);
            }
        for (int i = 0; i < SZ(anita); i++) {
            ++vis[anita[i]];
            if (vis[anita[i]] == 2) take++, carol = anita[i];
        }
        if (take == 1) printf("%d\n", carol);
        if (take > 1) printf("Bad magician!\n");
        if (take < 1) printf("Volunteer cheated!\n");
    }
    
    return 0;
}
