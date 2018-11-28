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
#define maxn 3000
int n;
int A[maxn], B[maxn];
int res[maxn];
bool dd[maxn];
int a[maxn], b[maxn], pos[maxn];
bool found;

bool valid(int id) {
    FOR(i,1,id-1)
    if (res[i] < res[id] && A[i] >= A[id]) return false;
    FOR(i,1,id-1)
    if (res[i] > res[id] && B[i] <= B[id]) return false;

    FOR(i,1,id) {
        a[i] = 1;
        FOR(j,1,i-1) if (res[i] > res[j]) a[i] = max(a[i], a[j] + 1);
        if (a[i] != A[i]) return false;
    }
    DOWN(i,id,1) {
        b[i] = 1;
        FOR(j,i+1,id) if (res[i] > res[j]) b[i] = max(b[i], b[j] + 1);
        if (b[i] > B[i]) return false;
    }
    FOR(i,1,n)
    if (dd[i]) break;
    else {
        if (b[pos[i]] != B[pos[i]]) return false;
    }
    DOWN(i,id,1) {
        int cnt = 0;
        FOR(t,1,res[i]-1) if (dd[t]) cnt++;
        b[i] = cnt + 1;
        FOR(j,i+1,id) if (res[i] > res[j]) b[i] = max(b[i], b[j] + 1);
        if (b[i] < B[i]) return false;
    }
    FOR(i,1,id)
    FOR(j,id+1,n) {
        if (A[i] >= A[j]) {
            bool ok = false;
            FOR(t,1,res[i]-1)
            if (dd[t]) {
                ok = true;
                break;
            }
            if (!ok) return false;
        }
        if (B[i] <= B[j]) {
            bool ok = false;
            FOR(t,res[i]+1,n)
            if (dd[t]) {
                ok = true;
                break;
            }
            if (!ok) return false;
        }
    }
    return true;
}
bool correct_state() {
    FOR(i,1,n) {
        a[i] = 1;
        FOR(j,1,i-1) if (res[j] < res[i]) a[i] = max(a[i], a[j] + 1);
        if (a[i] != A[i]) return false;
    }
    DOWN(i,n,1) {
        b[i] = 1;
        FOR(j,i+1,n) if (res[i] > res[j]) b[i] = max(b[i], b[j] + 1);
        if (b[i] != B[i]) return false;
    }
    return true;
}
void attempt(int cur) {
    if (cur == n+1) {
        if (correct_state()) {
            found = true;
            FOR(i,1,n) cout << " " << res[i];
        }
        return;
    }
    FOR(i,1,n)
    if (dd[i]) {
        if (found) return;
        res[cur] = i;
        dd[i] = false;
        pos[i] = cur;
        if (!valid(cur)) {
            dd[i] = true;
            continue;
        }
        attempt(cur+1);
        if (found) return;
        dd[i] = true;
    }

}
void solve() {
    memset(dd,true,sizeof(dd));
    memset(res,0,sizeof(res));

    found = false;
    memset(pos,0,sizeof(pos));
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    attempt(1);
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cerr << test << endl;
        cout << "Case #" << test << ":";
        cin >> n;
        FOR(i,1,n) cin >> A[i];
        FOR(i,1,n) cin >> B[i];
        solve();
        cout << endl;
    }
    return 0;
}
