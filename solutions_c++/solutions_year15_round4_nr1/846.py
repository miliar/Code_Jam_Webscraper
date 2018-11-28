/* Divanshu Garg */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%llu",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
ill ABS(ill a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
}

/* Input opener ends */

int n;
int a[1123456];

string s[105];

// < - 0
// > - 1
// ^ - 2
// v - 3

int main() {
    input();

    int t, kase = 1; cin >> t;
    while ( t-- ) {

        int n, m; cin >> n >> m;
        int poss = 1;
        F(i,0,n) {
            cin >> s[i];
        }

        F(i,0,n) F(j,0,m) {
            if ( s[i][j] == '.' ) continue;
            int c = 0;
            F(k,0,m) c += (s[i][k] != '.');
            F(k,0,n) c += (s[k][j] != '.');
            if ( c <= 2 ) poss = 0; 
        }

        if ( !poss ) {
            printf("Case #%d: IMPOSSIBLE\n", kase++);
            continue;
        }

        int ans = 0;

        F(i,0,n) {
            F(j,0,m) {
                if ( s[i][j] == '.' ) continue;
                int val[4];
                F(k,0,4) val[k] = 1;
                // int fic = 1, fir = 1, lic = 1, lir = 1;
                F(k,0,j) if ( s[i][k] != '.' ) val[0] = 0;
                F(k,j+1,m) if ( s[i][k] != '.' ) val[1] = 0;
                F(k,0,i) if ( s[k][j] != '.' ) val[2] = 0;
                F(k,i+1,n) if ( s[k][j] != '.' ) val[3] = 0; 

                int x = 0;
                if ( s[i][j] == '>' ) x = 1;
                if ( s[i][j] == '^' ) x = 2;
                if ( s[i][j] == 'v' ) x = 3;

                if ( val[x] == 1 ) ans++;

            }
        }

        printf("Case #%d: %d\n", kase++, ans);        

    }

    return 0;
}


