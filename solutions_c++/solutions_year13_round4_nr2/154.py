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
long long N,P;

long long get_worst_rank(long long each_half, long long sl) {
    if (sl == 1) return 1;
    return each_half + get_worst_rank(each_half/2,sl/2);
}
bool check_worst(long long id) {
    long long cur_rank = get_worst_rank(1LL<<(N-1),id+1);
    return cur_rank <= P;
}
void solve_for_worst() {
    long long first = 0, last = (1LL << N) - 1, mid;
    do {
        mid = (first + last) / 2;
        if (check_worst(mid)) first = mid;
        else last = mid;
    } while (last - first > 1);
    if (check_worst(last)) cout << last << " ";
    else cout << first << " " ;
}

long long get_best_rank(long long each_half, long long sl) {
    if (sl == 1) return each_half*2;
    return get_best_rank(each_half/2,sl/2);
}
bool check_best(long long id) {
    long long cur_rank = get_best_rank(1LL<<(N-1),(1LL<<N)-id);
    return cur_rank <= P;
}
void solve_for_best() {
    long long first = 0, last = (1LL << N) - 1, mid;
    do {
        mid = (first + last) / 2;
        if (check_best(mid)) first = mid;
        else last = mid;
    } while (last - first > 1);
    if (check_best(last)) cout << last;
    else cout << first ;
}

void solve() {
    solve_for_worst();
    solve_for_best();
    cout << endl;
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> N >> P;
        solve();
    }
    return 0;
}
