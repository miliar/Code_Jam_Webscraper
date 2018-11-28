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

int ntc;
double C, F, X;

int main() {
    scanf("%d", &ntc);
    
    for ( int tc = 0; tc < ntc; tc++ ) {
        scanf("%lf%lf%lf", &C, &F, &X);
        
        double rate = 2, tott = 0;
        while ( true ) {
            double ttw = X/rate, ttf = C/rate + X/(rate+F);
            // printf("rate=%.3lf, ttw=%.3lf, ttf=%.3lf\n", rate, ttw, ttf);
            if ( ttw < ttf ) {
                tott += ttw;
                break;
            }
            else {
                tott += C/rate;
                rate += F;
            }
        }
        
        printf("Case #%d: %.7lf\n", tc+1, tott);
    }
    
    return 0;
}
