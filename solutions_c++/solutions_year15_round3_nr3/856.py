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
#define maxn 40
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp(x,y) make_pair(x, y)

long long c, d, v, cnt, numtest, n, res, vt;
vector<long long> vv;
long long a[maxn];
bool have[maxn];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("C-small-attempt1.in","r",stdin);
    freopen("ou.out","w",stdout);
    #endif

    cin >> numtest;
    fto(test, 1, numtest) {
        cin >> c >>  d >> v;
        fto(i,1,d) cin >> a[i];

        vv.clear();
        fto(i,0,30) have[i] = false;

        fto(i,1,d) {
            n = vv.size()-1;
            fto(j,0,n)
                if (a[i]+vv[j]<=v) {
                    vv.push_back(a[i]+vv[j]);
                    have[a[i]+vv[j]] = true;
            }
            vv.push_back(a[i]);
            if (a[i]<=v) have[a[i]] = true;
        }

        res = 0;
        while (1) {
            cnt = 0;
            fto(i,1,v)
                if (have[i]==true) cnt++;
                else {
                    vt = i;
                    break;
                }

        //    debug(vt);
            if (cnt==v) break;
            res++;
            n = vv.size()-1;
            fto(j,0,n)
                if (vv[j]+vt<=v) {
                    vv.push_back(vv[j]+vt);
                    have[vv[j]+vt] = true;
                }
            vv.push_back(vt);
            have[vt] = true;
        }


      //  fto(i,0,vv.size()-1) cout << vv[i] << " ";
     //   cout << endl;
     //   debug(cnt);

        cout << "Case #" << test << ": " << res << endl;
    }

}
