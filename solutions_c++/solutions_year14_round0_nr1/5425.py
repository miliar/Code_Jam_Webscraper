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
    int r1, r2;
    int a[4][4], b[4][4];    
    scanf("%d", &r1);
    rept(i, 4)
        rept(j, 4)
            scanf("%d", &a[i][j]);
    scanf("%d", &r2);
    rept(i, 4)
        rept(j, 4)
            scanf("%d", &b[i][j]);
    r1--;
    r2--;
    vector<int> s;
    rept(i, 4)
        rept(j, 4)
            if (a[r1][i] == b[r2][j]) {
                s.pb(a[r1][i]);
            }
    printf("Case #%d: ", case_id);
    if (s.size() == 0) {
        printf("Volunteer cheated!\n");
    } else if (s.size() == 1) {
        printf("%d\n", s[0]);
    } else {
        printf("Bad magician!\n");
    }
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
