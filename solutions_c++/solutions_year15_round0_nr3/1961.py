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

map<pair<char, char>, char> m, signc;
int numtest, x, l, posi, posk;
char multi, signmulti;
string s;

int calc(char t) {
    if (signmulti=='-' && signc[mp(multi,t)]=='-') signmulti = '+';
    else if (signmulti=='+' && signc[mp(multi,t)]=='-') signmulti = '-';
    multi = m[mp(multi,t)];
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("C-small-attempt2.in","r",stdin);
    //freopen("in.inp","r",stdin);

    freopen("ou.out","w",stdout);
    #endif

    m[mp('1','1')] = '1';
    m[mp('1','i')] = 'i';
    m[mp('1','j')] = 'j';
    m[mp('1','k')] = 'k';
    m[mp('i','1')] = 'i';
    m[mp('i','i')] = '1';
    m[mp('i','j')] = 'k';
    m[mp('i','k')] = 'j';
    m[mp('j','1')] = 'j';
    m[mp('j','i')] = 'k';
    m[mp('j','j')] = '1';
    m[mp('j','k')] = 'i';
    m[mp('k','1')] = 'k';
    m[mp('k','i')] = 'j';
    m[mp('k','j')] = 'i';
    m[mp('k','k')] = '1';

    signc[mp('1','1')] = '1';
    signc[mp('1','i')] = 'i';
    signc[mp('1','j')] = 'j';
    signc[mp('1','k')] = 'k';
    signc[mp('i','1')] = 'i';
    signc[mp('i','i')] = '-';
    signc[mp('i','j')] = 'k';
    signc[mp('i','k')] = '-';
    signc[mp('j','1')] = 'j';
    signc[mp('j','i')] = '-';
    signc[mp('j','j')] = '-';
    signc[mp('j','k')] = 'i';
    signc[mp('k','1')] = 'k';
    signc[mp('k','i')] = 'j';
    signc[mp('k','j')] = '-';
    signc[mp('k','k')] = '-';

    cin >> numtest;
    fto(test, 1, numtest) {
        cin >> x >> l;   getchar();
        getline(cin, s);

        posi = -1;   posk = -1;  multi = '1';  signmulti = '+';
        fto(j,1,l) {
            fto(i,0,s.length()-1) {
                //debug(m[mp('k','k')]);
                calc(s[i]);

             //   debug(s[i]);
             //   debug(multi);
             //   debug(signmulti);   cout << endl;
                if (multi=='k' && signmulti=='+') posk = i+s.length()*(j-1);
                if (multi=='i'&& posi==-1 && signmulti=='+') posi = i+s.length()*(j-1);
            }
        }
       // debug(posk);
        //debug(posi);

        if (multi!='1' || signmulti!='-' || posk==-1 || posi==-1) {
            cout << "Case #" << test << ": NO" << endl;
            continue;
        }

        if (posi<posk) cout << "Case #" << test << ": YES" << endl;
        else cout << "Case #" << test << ": NO" << endl;
    }
}
