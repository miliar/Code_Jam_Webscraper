#include <cstdio>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <bitset>

#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

using namespace std;

typedef long long ll;
typedef unsigned long long llu;

int main(){
    int test, ks;
    int isOk[17], grid[4][4], n;
    
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    while ( scanf("%d", &test) == 1 ){
        for ( ks = 1 ; ks <= test ; ks++ ){
            memset(isOk, 0, sizeof(isOk));
            
            scanf("%d", &n);
            n--;
            for ( int i = 0 ; i < 4 ; i++ )
                for ( int j = 0 ; j < 4 ; j++ )
                    scanf("%d", &grid[i][j]);

            for ( int i = 0 ; i < 4 ; i++ )
                isOk[grid[n][i]]++;

            scanf("%d", &n);
            n--;
            for ( int i = 0 ; i < 4 ; i++ )
                for ( int j = 0 ; j < 4 ; j++ )
                    scanf("%d", &grid[i][j]);

            for ( int i = 0 ; i < 4 ; i++ )
                isOk[grid[n][i]]++;

            vector<int> final;
            for ( int i = 1 ; i <= 16 ; i++ ) if (isOk[i] == 2 ) final.push_back(i);
            
            printf("Case #%d: ", ks);
            if ( final.size() == 0 ) puts("Volunteer cheated!");
            else if ( final.size() == 1 ) printf("%d\n", final[0]);
            else puts("Bad magician!");
        }
    }
    
    return 0;
}
