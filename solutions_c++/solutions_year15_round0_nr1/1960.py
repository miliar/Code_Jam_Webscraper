#include <bits/stdc++.h>
using namespace std;

#define fto(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define fdw(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define out(x,y) cout << x << y
#define out3(x,y,z) cout << x << y << z
#define debug(a) cout << #a << " = " << a << endl
#define debuga(t,n) for (int i = 1; i<=n; i++) cout << t[i]<< " "
#define ooLL 1000000000000LL
#define oo 1000000000
#define maxn 100005
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp(x,y) make_pair(x, y)

int test, num, smax, numtest;
long long res;
char c;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif

    cin >> numtest;
    fto(test, 1, numtest) {
        cin >> smax;   getchar();
        num = 0;   res = 0;
        fto(i,0,smax) {
            c = getchar();
            //debug(c);
            if (num>=i) num += (c-'0');
            else {
                res += (i-num);
                num = i + (c-'0');
            }
           // debug(num);
        }
        cout << "Case #" << test << ": " << res << endl;
    }
}
