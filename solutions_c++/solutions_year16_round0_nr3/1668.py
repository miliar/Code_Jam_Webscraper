#include <bits/stdc++.h>

using namespace std;


#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pii pair < int, int >
#define pll pair < ll, ll >
#define all(s) s.begin(), s.end()
#define sz(s) (int) s.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;

vector < ll > g[1<<20];
vector < ll > gr[1<<20];
vector < ll > A[55];
int NN = 13;

ll getDiv(ll x){
    for (ll i=2;i*1ll*i<=x;i++){
        if (x%i == 0) return i;
    }
    return 1;
}

ll get(ll base, ll mask){
    ll res = 0;
    ll p = 1;
    for (int i=0;i<NN;i++){
        if (mask&(1<<i)){
            res += p;
        }
        p *= base;
    }
    return res;
}

bool check(int mask){
    bool ok = true;
    for (int base=2;base<=10;base++){
        ll res = get(base, mask);
        if (getDiv(res) == 1){
            ok = false;
            break;
        }
    }
    return ok;    
}

int getlen(ll mask){
    for (int i=60;i>=0;i--){
        if (mask&(1ll<<i)) return i + 1;
    }
    return 0;
}

void precalc(){
    for (int mask=3;mask<(1<<NN);mask+=2){   
        int len = getlen(mask);
        if (check(mask)){
            if (sz(A[len]) < 500)
                A[len].pb(mask);
        }
    }
}


string toBase2(ll mask){
    ll len = getlen(mask);
    string s = "";
    for (int i=0;i<len;i++){
        s += char(((mask&(1ll<<i))>0) + '0');
    }
    reverse(all(s));
    return s;
}

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif

    precalc();
    int T, N, J;
    scanf("%d%d%d", &T, &N, &J);

    cout <<"Case #1:"<<endl;

    if (N < NN){
        for (int i=0;i<min(sz(A[N]), J);i++){
            ll t = A[N][i];
            string s = toBase2(t);
            cout <<s<<" ";
            for (int base=2;base<=10;base++){
                cout <<getDiv(get(base, t))<<" ";
            }
            cout <<endl;
        }
        return 0;
    }

    int M = 10;
    for (int mask1=3;mask1<(1<<M);mask1++){
        for (int mask2=3;mask2<(1<<M);mask2++){
            bool ok = true;
            for (int base=2;base<=10;base++){
                ll t1 = get(base, mask1);
                ll t2 = get(base, mask2);
                if (t1%t2 != 0){
                    ok = false;
                    break;
                }
            }
            if (ok){
                g[mask1].pb(mask2);
                gr[mask2].pb(mask1);
            }
        }
    }

    set < ll > S;
    vector < pair < ll, ll > > ans;

    for (int mask=3;mask<(1<<M);mask+=2){
        forit(it, gr[mask]){
            int len = getlen(*it) + getlen(mask);
            if (len <= N){
                ll shift = N - len;
                ll nval = ((*it)<<(shift + getlen(mask))) + mask;
                if (sz(ans) < J && S.find(nval) == S.end()){
                    ans.pb(mp(nval, mask));
                    S.insert(nval);
                }
            }
        }
    }

    for (int i=0;i<min(sz(ans), J);i++){
        ll t = ans[i].f;
        ll x = ans[i].s;
        string s = toBase2(t);
        cout <<s<<" ";
        for (int base=2;base<=10;base++){
            cout <<get(base, x)<<" ";
        }
        cout <<endl;        
    }


    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
