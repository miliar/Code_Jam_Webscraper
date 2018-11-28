#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <cmath>
#include <set>
#include <utility>

#define eps 1e-9
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define sz(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define ms(x,i) memset((x),(i),sizeof((x)))
#define debug(x) if(DEBUG) cout << x << endl
#define DEBUG 1

using namespace std;

typedef long long ll;
typedef pair<int,int> pt;
typedef pair<pt,int> ppt;
const int nmax = 1010;
set <double> warNaomi, warKen, Naomi, Ken;
set <double> :: iterator itNaomi, itKen;
int t, n;
double a;
void input() {
    warNaomi.clear();
    warKen.clear();
    Naomi.clear();
    Ken.clear();

    scanf("%d", &n);
    FOR(i,1,n) {
        scanf("%lf", &a);
        warNaomi.insert(a);
    }
    FOR(i,1,n) {
        scanf("%lf", &a);
        warKen.insert(a);
    }
    Naomi = warNaomi;
    Ken = warKen;
}

int solveWar() {
    int point = 0;
    int i = 0;
    for(itNaomi = warNaomi.begin(); itNaomi != warNaomi.end(); itNaomi++) {
        i++;
        if(*itNaomi > *(warKen.rbegin())) {
            point += n - i + 1;
            break;
        }
        else warKen.erase(upper_bound(ALL(warKen), *itNaomi));
    }
    return point;
}

int solveDeceitfulWar() {
    int point = 0;
    while(!Naomi.empty()) {
        itKen = Ken.end();
        itNaomi = Naomi.end();

        itKen--;
        itNaomi--;

        if(*itNaomi > *itKen) {
            Naomi.erase(itNaomi);
            point++;
        }
        else Naomi.erase(Naomi.begin());
        Ken.erase(itKen);
    }
    return point;
}

void solve(int test) {
    //cout << "Case #" << test << ": ";
    input();
    int y, z;
    y = solveDeceitfulWar();
    z = solveWar();
    printf("Case #%d: %d %d\n", test, y, z);
    //cout << y << " " << z << endl;
}
int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out","w",stdout);
    //std::ios::sync_with_stdio(false);
    scanf("%d", &t);
    FOR(i,1,t) {
        solve(i);
    }
    return 0;
}
