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

long long num, numtest, res, n, maxa, cnt, best;
int a[maxn];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif

    cin >> numtest;
    fto(test,1,numtest) {
        cin >> n;

        maxa = -1;
        fto(i,1,n) {
            cin >> a[i];
            if (maxa<a[i]) maxa = a[i];
        }

        best = oo;
        fto(maxpan,1,maxa) {
            cnt = 0;
            fto(i,1,n) {
                if (a[i]>maxpan)
                    if (a[i]%maxpan!=0) cnt += a[i]/maxpan;
                    else cnt += a[i]/maxpan - 1;
            }
            if (best>cnt+maxpan) best = cnt+maxpan;
        }
        cout << "Case #" << test << ": " << best << endl;
    }
}
