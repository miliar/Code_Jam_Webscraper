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
int n;
long long B, a[50];

void solve() {
    vector<int> ds(0);
    FOR(i,1,n) ds.push_back(a[i]);
    sort(a+1,a+n+1);
    a[n+1] = 1000000000000000000LL;
    a[0] =0 ;
    FOR(i,0,n) {
        long long threshold = a[i];
        long long money_left = B;
        int cnt = 37 - n;
        money_left -= cnt * threshold;
        FOR(j,1,n)
        if (a[j] <= threshold) money_left -= (threshold - a[j]), cnt++;
        if (money_left < 0) continue;
        if (cnt > 0) {
            ds.push_back(threshold + money_left / cnt);
            ds.push_back(threshold + money_left / cnt - 1);
            ds.push_back(threshold + money_left / cnt + 1);
        }
    }
    ds.push_back(0);
    FOR(i,0,n) if (a[i] > 0) ds.push_back(a[i] - 1);
    FOR(i,0,n) ds.push_back(a[i]+1);
    long double res = 0;
    FOR(i,0,10000) {
        long long threshold = i;
        long long money_left = B;
        money_left -= (37 - n) * threshold;
        int cnt = (37 - n);
        FOR(j,1,n)
        if (a[j] <= threshold) money_left -= (threshold - a[j]), cnt++;
        if (money_left < 0) continue;
        long double expected_money = 0;
        FOR(j,1,n)
        if (a[j] <= threshold) expected_money += (money_left + 36 * (threshold-a[j]) - B) * 1.0 /cnt;

        expected_money += (money_left + 36 * threshold - B) * (double)(37-n)/cnt;
        res = max(res, expected_money);

        vector<long long> ls(0);
        FOR(j,1,n)
        if (a[j] <= threshold) ls.push_back(threshold-a[j]);
        FOR(j,1,37-n) ls.push_back(threshold);
        sort(ls.begin(),ls.end());
        cnt = ls.size();
        FOR(t,1,money_left) {
            cnt--;
            if (cnt == 0) break;
            long double expected_money = 0;
            int skipped = t;
            FR(j,ls.size()) {
                if (skipped) {
                    skipped--;
                    continue;
                }
                expected_money += (money_left - t + 36 * ls[j] - B) * 1.0 /cnt;
            }
            res = max(res, expected_money);
        }
    }
    printf("%.9lf\n",(double)res);
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> B >> n;
        FOR(i,1,n) cin >> a[i];
        solve();
    }
    return 0;
}
