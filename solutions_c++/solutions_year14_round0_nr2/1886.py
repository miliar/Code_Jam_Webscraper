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

int itc, ntc;
double c,f,x, rate, carol, anita;


int main() {
    OPEN("B");
    scanf("%d", &ntc);
    for (int itc = 0; itc < ntc; itc++) {
        printf("Case #%d: ", itc+1);
        scanf("%lf%lf%lf", &c, &f, &x);
        anita = x/2; carol = 0; rate = 2.0;
        for (int i = 0; i < 100000000; i++) {
            if (anita < carol + x/rate) break;
            MN(anita, carol + x/rate);
            carol += c/rate; rate += f;
        }
        printf("%.7lf\n", anita);
    }
    return 0;
}
