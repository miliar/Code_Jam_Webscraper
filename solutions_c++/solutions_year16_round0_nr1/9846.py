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

int check[10];
int cnt;

int solve(int n) {
    if(n == 0)
        return 0;
    
    FOR(i, 1, 1e10) {
        int x = n*i;
        
        while(x) {
            int a = x % 10;
            
            if(!check[a]) {
                cnt++;
                check[a] = 1;
            }
            
            x /= 10;
        }
        
        if(cnt == 10)
            return n*i;
    }
    
    return 0;
}

int main() {
    int t;
    int n;
    
    scanf("%d", &t);
    
    REP(i, t) {
        CLR(check);
        cnt=0;
        
        scanf("%d", &n);
        
        int ans = solve(n);
        
        if(ans) {
            printf("Case #%d: %d\n", i+1, ans);
        }
        else {
            printf("Case #%d: INSOMNIA\n", i+1);
        }
    }
    
    return 0;
}
