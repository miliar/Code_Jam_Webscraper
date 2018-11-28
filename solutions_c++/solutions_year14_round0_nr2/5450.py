#ifdef SHTRIX 
#include "/Users/roman/Dev/SharedCpp/DebugOutput.h"
#endif
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())


void solve(int case_id) {
    double c, f, x;
    cin >> c >> f >> x;
    int p = max(0.0, x / c - 2 / f + 1e-9);
//    cerr << p << endl;
    double t = 0.0;
    rept(i, p) {
        t += c / (2 + i * f);
    }
    t += x / (2 + p * f);
    printf("Case #%d: %.9lf\n", case_id, t);
}

int main()
{
    #ifdef SHTRIX 
    freopen("input.txt","rt",stdin); 
    //freopen("output.txt","wt",stdout); 
    #endif
	int TC;
    scanf("%d", &TC);
    rep(tc, TC) {
        solve(tc);
    }
    return 0;
}
