#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define EPS 1e-14
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset((a),(c),sizeof (a))
#define CLR(a) memset((a),0,sizeof (a))

using namespace std;

char str[100];

int solve(string s) {
    int l = s.length();
    
    // p : i番目までを全て'+'にするのに必要な回数
    // m : i番目までを全て'-'にするのに必要な回数
    int p = 0;
    int m = 0;
    
    REP(i, l) {
        int c = s[i];
        
        if(c == '+') {
            //p = p;
            m = p+1;
        }
        else {
            p = m+1;
            // m = m;
        }
    }
    
    return p;
}

int main() {
    int t;
    string str;
    
    cin >> t;
    
    REP(i, t) {
        cin >> str;
        
        int ans = solve(str);
        printf("Case #%d: %d\n", i+1, ans);
    }
    
    return 0;
}
