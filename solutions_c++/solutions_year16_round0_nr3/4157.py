#include <bits/stdc++.h>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl

using namespace std;

typedef pair<int,int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const double PI = 2*acos(0.0);
const double eps = 1e-9;
const int infi = 1e9;
const LL Linfi = (LL) 1e18;
const LL MOD = 1000000007;
#define maxn 10000005

int n, k;
bool d[maxn];
int xet[1000005];
LL BASE[10][20];

/** This function calculates (ab)%c */
LL mulmod(LL a,LL b,LL c){
    LL x = 0,y = a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}

LL power_mod(LL a, LL b, LL c){
    long long x=1, y=a;
    while(b > 0){
        if(b%2 == 1){
            x = mulmod(x%c, y%c, c);
        }
        y = mulmod(y%c, y%c, c);
        b /= 2;
    }
    return x%c;
}

const int PRIME[] = {2, 3, 5, 7, 11, 13, 17, 19,
    23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71};

bool rabinMiller(LL x, int numTry = 15) {
  LL k = x - 1;
  int m = 0;
  for (; (k & 1) == 0; k >>= 1, m++);
  for (int i = 0; i < numTry && PRIME[i] < x; i++) {
    LL t = power_mod(PRIME[i], k, x);
    if (t == 1 || t == x - 1) {
      continue;
    }
    for (int j = 0; j < m && t != x - 1; j++) {
      t = mulmod(t, t, x);
    }
    if (t != x - 1) {
      return false;
    }
  }
  return true;
}

int sang(int n){
    memset(d, 0, sizeof(d));
    FOR(i,2,sqrt(n)){
        if(d[i] == 0){
            for(int j = i*i; j <= n; j += i)
                d[j] = 1;
        }
    }
}

int finalPrime(LL n){
    if(n <= maxn-1) return d[n] == 0 ? 1 : 0;
    return rabinMiller(n, 15);
    return 1;
}

int checkOneBase(int mask, int d){
    LL cur = 0;
    FORD(i,n-1,0) {
        if(getbit(mask,i)) cur += BASE[d][i];
    }
    return finalPrime(cur) == 0;
}

int checkFullBase(int mask){
    FOR(i,2,10) if(checkOneBase(mask,i) == 0) return 0;
    return 1;
}

int check9(int mask){
    LL cur = 0;
    FORD(i,n-1,0) {
        if(getbit(mask,i)) cur += BASE[9][i];
    }
    FOR(i,2,1000000) if(cur%i == 0) return 1;
    return 0;
}

int check10(int mask){
    LL cur = 0;
    FORD(i,n-1,0) {
        if(getbit(mask,i)) cur += BASE[10][i];
    }
    FOR(i,2,1000000) if(cur%i == 0) return 1;
    return 0;
}

void solve() {
    sang(maxn-5);
    FOR(i,2,10){
        BASE[i][0] = 1;
        FOR(j,1,n) BASE[i][j] = BASE[i][j-1]*i;
    }
    //cout << checkFullBase(33) << endl;
    /// process

    vector<int> ans;
    FOR(step,1,k){
        while(1){
            int tmp = rand();
            FOR(i,n-1,16) tmp = offbit(tmp, i);
            tmp = onbit(tmp, n-1);
            tmp = onbit(tmp, 0);

            if(checkFullBase(tmp) && xet[tmp] == 0 && check9(tmp) && check10(tmp)) {
                xet[tmp] = 1;
//                FORD(i,n-1,0) {
//                    if(getbit(tmp, i)) cout << 1 << " ";
//                    else cout << 0 << " ";
//                }
//                cout << tmp << endl;
                ans.pb(tmp);
                break;
            }
            else xet[tmp] = -1;
        }
    }

    /// print ans
    FO(t,0,ans.size()){
        int mask = ans[t]; LL last = 0;
        vector<int> V;
        FOR(d,2,10){
            LL cur = 0;
            FORD(i,n-1,0) {
                if(getbit(mask,i)) cur += BASE[d][i];
            }
            last = cur;

            //cout << cur << "  ";
            FOR(i,2,10000000){
                if(cur%i == 0){
                    V.pb(i);
                    //cout << d << " " << i << endl;
                    break;
                }
            }
        }
        cout << last;
        FO(i,0,V.size()) cout << " " << V[i];
        //if(V.size() < 9) debug;
        cout << endl;
    }
}

int main(){
    srand(time(0));
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> n >> k;
        cout << "Case #" << test << ":\n";
        solve();
    }

    //cout << rabinMiller(36680094401, 15) << endl;

    return 0;
}


