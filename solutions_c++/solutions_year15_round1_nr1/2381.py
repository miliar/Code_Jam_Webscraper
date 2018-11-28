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
#define maxn 2000
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp(x,y) make_pair(x, y)

int a[maxn];
int numtest, n;
long long res1 , res2, speed;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large (1).in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif

    cin >> numtest;
    fto(test,1,numtest) {
        cin >> n;
        fto(i,1,n) cin >> a[i];

        res1 = 0;
        res2 = 0;
        speed = 0;
        fto(i,1,n-1) {
            if (a[i]-a[i+1]>0) {
                res1 += a[i]-a[i+1];
                if (speed<a[i]-a[i+1]) speed = a[i]-a[i+1];
            }
        }

        fto(i,1,n-1)
            if (a[i]<speed) res2 += a[i];
            else res2 += speed;

//        if (res2<0) res2 = 0;
        cout << "Case #" << test << ": " << res1 << " " << res2 << endl;
    }
}
