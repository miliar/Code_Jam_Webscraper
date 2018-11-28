#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,n) for(int i=a,_n=n; i<=_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define ALL(v) (v).begin(), (v).end()

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int tcase; scanf("%d", &tcase);
    
    int n;
    int dummy;
    int naomi[1002], ken[1002];
    REP (x, tcase) {
        scanf("%d", &n);
        REP (i, n) scanf("%d.%d", &dummy, &naomi[i]);
        REP (i, n) scanf("%d.%d", &dummy, &ken[i]);
        
        sort(naomi, naomi+n, greater<int>());
        sort(ken, ken+n, greater<int>());
        
        //deceitful
        int deceitful = 0;
        int kindex = n-1; int nindex = n-1;
        REP (i, n) {
            int naomis = naomi[nindex];
            int kens = ken[kindex];
            
            if ( naomis > kens ) {
               ++deceitful;   
               --kindex;
            }    
            
            --nindex;
        }
        
        //undeceitful
        int undeceitful = 0;
        nindex = 0; 
        int bkindex = 0;
        
        REP (i, n) {
            int naomis = naomi[nindex];
            int bigken = ken[bkindex];
            
            if ( naomis > bigken ) {
               ++undeceitful; 
            }         
            else {
                 ++bkindex;
            }
            ++nindex;       
        }
        printf("Case #%d: %d %d\n", x+1, deceitful, undeceitful);
    }

   return 0;
}
