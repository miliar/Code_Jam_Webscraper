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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;

#define MAX 105

typedef long long ll;

int main() {
    int T;
    cin >> T;
    REPN(tc, 1, T+1) {
        double C, F, X;

        cin >> C >> F >> X;

        double res = X / 2.0;
        int cF = 1;
        double B = 0, A;
        double dife = 0.0;

        while (fabs(dife - res) >= 1e-9) {
            dife = res;
            A = X / (2 + cF*F);
            B += C / (2 + (cF-1)*F);
            res = min(res, A + B);
            cF++;
        }

        printf("Case #%d: %.7f\n", tc, res);
        //cout << "Case #" << tc << ": " << res << "\n";
    }
}

