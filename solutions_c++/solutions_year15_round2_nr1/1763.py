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
#define maxn 1000005
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp(x,y) make_pair(x, y)

int f[maxn];
int n,numtest;

int swapt(int x) {
    int y = x, num = 0;
    if (y%10==0) return oo;
    while (y>0) {
        num = num*10 + y%10;
        y /= 10;
    }
    return num;
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif


    cin >> numtest;
    fto(test, 1, numtest) {
        cin >> n;
        fto(i,1,n) f[i] = 0;
        f[1] = 1;
        fto(i,2,n)
            if (swapt(i)<i) {
                f[i] = min(f[i-1]+1,f[swapt(i)]+1);
              //  debug(swapt(i));
              //  debug(i);
            }
            else f[i] = f[i-1]+1;

        cout << "Case #" << test << ": " << f[n] << endl;
    }
}
