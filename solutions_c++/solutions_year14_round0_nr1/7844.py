#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
 
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
 
#define INF 2000000000
#define EPS 1e-9
#define sz(c) (int) (c).size()
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define uniq(c) sort(all(c)); (c).resize(unique(all(c)) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all(c), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all(c), (x)) - (c).begin())
 
#define pb push_back
#define mp make_pair
#define fi first
#define se second
 
using namespace std;
 
typedef long long ll;
typedef pair <int, int> ii;

const int MAXC = 4;
int ntc, gs[2], card[2][5][5];

int main() {
    scanf("%d", &ntc);
    
    for ( int tc = 0; tc < ntc; tc++ ) {
        for ( int turn = 0; turn < 2; turn++ ) {
            scanf("%d", &gs[turn]);
            gs[turn]--;
            
            for ( int i = 0; i < MAXC; i++ ) 
                for ( int j = 0; j < MAXC; j++ ) 
                       scanf("%d", &card[turn][i][j]);
        }
        
        // for ( int i = 0; i < MAXC; i++ ) { for ( int j = 0; j < MAXC; j++ ) printf("[%d]", card[0][i][j]); puts(""); }
        
        vector <int> ans;
        // match turn 1 to turn 2
        for ( int j = 0; j < MAXC; j++ ) {
            bool found = false;
            for ( int jj = 0; jj < MAXC; jj++ ) 
                if ( card[0][gs[0]][j] == card[1][gs[1]][jj] ) {
                    // printf("card[%d][%d]=%d, card[%d][%d]=%d\n", gs[0], j, card[0][gs[0]][j], gs[1], jj, card[1][gs[1]][jj]);
                    found = true; break;
                }
            
            if ( found ) ans.pb(card[0][gs[0]][j]);
        }
        
        printf("Case #%d: ", tc+1);
        if ( ans.empty() ) {
            printf("Volunteer cheated!\n");
        }
        else if ( sz(ans) > 1 ) {
            printf("Bad magician!\n");
        }
        else {
            printf("%d\n", ans[0]);
        }
    }
    
    return 0;
}
