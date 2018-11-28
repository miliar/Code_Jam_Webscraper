#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <ostream>
#include <queue>
#include <cmath>
#include <climits>
#include <utility>
#include <fstream>
#include <memory>
#include <sstream>
#include <set>
#include <iterator>
#include <iomanip>
#include <map>
#include <stack>
using namespace std;
#define FOR(a, b, n) for(int (a) = (b); (a) < (n); ++(a))
#define FORE(a, b, n) for(int (a) = (b); (a) <= (n); ++(a))
#define ITE(a, v) for(auto (a) = v.begin(); (a) != v.end(); ++(a))
#define LL long long
#define ALL(v) v.begin(),v.end()
#define ZERO(v) memset(v, 0, sizeof v)
#define NEG(v)  memset(v, -1, sizeof v)
#define F first
#define S second
#define LD long double
#define pw(x) (1LL << (x))
#define sqr(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define MOD 1000000007
#define PI 3.141592653589793
#define PII pair<LL, LL>
#define INF 0x3f3f3f3f
#define FUL(x) memset(x, 0x3f, sizeof(x));
#define debug(args...) {cerr << #args << " = "; errDebug(args); cerr << endl;}
void errDebug() {}
template<typename T, typename... Args>
void errDebug(T a, Args... args) {
    cerr << a << ' ';
    errDebug(args...);
}
LL n;
int k;
vector<LL> tmp;
LL mult_mod(LL a, LL b, LL c) {
    a %= c;
    b %= c;
    LL ret=0;
    while(b) {
        if(b&1) {
            ret += a;
            ret %= c;
        }
        a <<= 1;
        if(a >= c)
            a %= c;
        b >>= 1;
    }
    return ret;
}
LL fastpow(LL val, LL exp)
{
    if(exp == 0)
        return 1LL;
    LL v = fastpow(val, exp / 2);
    v = mult_mod(v,v,n);
    if(exp % 2 == 0)
        return v;
    return mult_mod(v,val,n) % n;
}
bool prime()
{
    if(n == 2)
        return true;
    if(n % 2 == 0)
        return false;
    if(n < 2)
        return true;
    LL u = n - 1;
    while(u % 2 == 0)
        u /= 2;
    int s = 30;
    FOR(i,0,s)
    {
        LL randNum = rand() % (n - 2) + 2;
        LL x = fastpow(randNum, u);
        while(u != n - 1)
        {
            LL y = (mult_mod(x,x,n)) % n;
            if(y == 1 && x != n- 1 && x != 1)
                return false;
            x = y;
            u *= 2;
        }
        if(x != 1)
            return false;
    }
    return true;
}
int nn;

LL find(LL val)
{
    for(LL i = 2; i <= sqrt(val) + 1; i++)
    {
        if(val % i == 0)
            return i;
    }
    return -1;
}
int check(int val)
{
    bool flag = true;
    tmp.clear();
    FORE(i,2,10)
    {
        n = 0;
        LL base = 1;
        LL v = val;
        while(v)
        {
            if(v & 1)
                n += base;
            base *= i;
            v /= 2;;
        }
        if(prime())
            flag = false;
        else
        {
            tmp.PB(n);
        }
    }
    if(flag)
    {
        vector<int> res;
        for(int i = 0; i < nn; i++, val >>= 1)
        {
            if(val & 1)
                res.PB(1);
            else
                res.PB(0);
        }
        for(int i = res.size() - 1; i>= 0; i--)
            cout << res[i];
        cout << " ";
        FOR(i,0, tmp.size())
        cout << find(tmp[i]) << " ";
        cout << endl;
        return 1;
    }
    return 0;
}

void solve()
{
    int cnt = 0;
    FOR(i,0,pw(nn))
    {
        if((i & 1) == 0)
            continue;
        if((i & (pw(nn - 1))) == 0)
            continue;
        cnt += check(i);
        if(cnt >= k)
           return;
    }
}
int main() {
    int T;
    cin >> T;
    FOR(h,0,T)
    {
        cin >> nn >> k;
        printf("Case #%d:\n", h + 1);
        solve();
    }
    return 0;
}