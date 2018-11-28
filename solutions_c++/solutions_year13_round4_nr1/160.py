//#pragma comment(linker, "/STACK:16777216")

#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <fstream>

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >=0; i--)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; i--)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair

#define F first
#define S second
#define RESET(c,x) memset(c,x,sizeof(c))
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()

#define REP(i,a) for(int i = 0; i < (a); i++)

#define sqr(x) ((x)*(x))
#define oo 1000000009
using namespace std;
/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
char bu[50];
string convertToString(int a) {
    sprintf(bu,"%d",a);
    return string(bu);
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y % 2) return (u * x) % Base; else return u;
}
void extended_euclid(long long A, long long B, long long &x,long long &y) {
    if (A == 1 && B == 0) {
        x = 1;
        y = 0;
        return;
    }
    if (A < B) extended_euclid(B,A,y,x);
    else {
        long long xx,yy;
        extended_euclid(A%B,B,xx,yy);
        x = xx;
        y = yy - (A/B)*xx;

    }
}
//newstate = (newstate-1) & oldstate
/*******************************CODE HERE***********************************/
#define maxn 10003
struct Segment {
    long long L,R,P;
};

long long Base = 1000002013LL;
long long m,n;
Segment a[maxn];
Segment b[maxn];
vector<long long> ds;
long long d[maxn];
long long get_interval(long long X, long long Y) {
    if (X > Y) return 0;
    return (Y * (Y+1) / 2 ) % Base- ((X-1) * X / 2)% Base;
}
void solve() {
    ds.clear();
    FOR(i,1,m) {
        ds.push_back(a[i].L);
        ds.push_back(a[i].R);
    }
    sort(ds.begin(),ds.end());
    ds.resize( unique(ds.begin(), ds.end()) - ds.begin());
    memset(d,0,sizeof(d));
    FOR(i,1,m) {
        b[i].L = lower_bound(ds.begin(),ds.end(), a[i].L) - ds.begin();
        b[i].R = lower_bound(ds.begin(),ds.end(), a[i].R) - ds.begin();
        FOR(j,b[i].L, b[i].R-1) d[j]+= a[i].P;
    }

    long long res = 0,total = 0;
    long long original_cost = 0;
    FOR(i,1,m) {
        original_cost = (original_cost + get_interval(n - (a[i].R - a[i].L) + 1, n) * a[i].P) % Base;
    }
    FR(i,ds.size())
    if (d[i]) {

        long long sl = d[i];
        long long cur = n;
        int j = i;
        long long total = 0;
        while (j < ds.size()) {
            //ket thuc hanh trinh o j
            long long delta = max(0LL, sl - d[j]);
            sl -= delta;
            if (sl) {
                total = (total + get_interval(cur - (ds[j+1] - ds[j]) + 1, cur) * sl) % Base;
                d[j] -= sl;
            }
            cur -= (ds[j+1] - ds[j]);
            if (!sl) break;
            j++;
        }
        res = (res + total)% Base;
    }
    res =(original_cost - res) % Base;
    if (res <0 ) res += Base;
    cout << res << endl;

}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> n >> m;
        FOR(i,1,m) cin >> a[i].L >> a[i].R >> a[i].P;
        solve();
    }
    return 0;
}
