#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl

bool vis[10];

int eval(int u) {
    CLR(vis, 0);
    int mul = 0, cnt = 0;
    while (cnt < 10) {
        mul++;
        int v = u*mul;
        while (v) {
            if (!vis[v%10]) vis[v%10] = true, cnt++;
            v /= 10;
        }
    }
    return mul*u;
}

int main() {

    ios_base::sync_with_stdio(false);

    int T, n;
    cin >> T;
    REP(tc, T) {
        cin >> n;
        if (n == 0) cout << "Case #" << tc+1 << ": " << "INSOMNIA\n";
        else cout << "Case #" << tc+1 << ": " << eval(n) <<"\n";
    }

    return 0;
}

