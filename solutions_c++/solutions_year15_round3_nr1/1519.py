#include <bits/stdc++.h>
using namespace std;

#define fto(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define fdw(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define out(x,y) cout << x << y
#define out3(x,y,z) cout << x << y << z
#define debug(a) cout << #a << " = " << a << endl
#define ooLL 1000000000000LL
#define oo 1000000000
#define maxn 100005
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp(x,y) make_pair(x, y)

long long numtest, res, c, w, r;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif

    cin >> numtest;
    fto(test, 1, numtest) {
        cin  >> r >> c >> w;
        res = (c-1)/w + w;
        cout << "Case #" << test << ": " << res << endl;
    }
}
