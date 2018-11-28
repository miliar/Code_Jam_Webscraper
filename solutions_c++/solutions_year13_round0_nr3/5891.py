#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <string.h>

#define INF                         (int)1e9
#define EPS                         1e-9

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define FOR(i,a,b)                  for(int i=a;i<b;i++)
#define REP(i,a)                    FOR(i, 0, a)
#define FOREACH(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define SORT(a)                     sort(all(a))
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define vout(x)                     FOREACH(_i, x) cout<< *_i << " "; cout << endl;
#define debug(x)                    cout << #x << " : " << x << endl;
#define checkbit(n,b)               ( (n >> b) & 1)
#define DREP(a)                     sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)              (lower_bound(all(arr),ind)-arr.begin())
#define LL                          long long
#define LD                          long double
#define VI                          vector<int>
#define VVI                         vector<VI>
#define VS                          vector<string>
#define PII                         pair<int,int>
#define VII                         vector<PII>

using namespace std;

bool is_palin(int no){
    int rev = 0, orig = no;
    while(no){
        rev = rev * 10 + (no % 10);
        no /= 10;
    }
    if(rev == orig)
        return true;
    return false;
}

bool is_square(int no){
    double d_sqrt = sqrt( no );
    int i_sqrt = d_sqrt;
    if ( d_sqrt == i_sqrt )
        return true;
    return false;
}

int main(){
    int T;
    cin >> T;
    FOR(tc, 1, T+1){
        int a, b, ct=0;
        cin >> a >> b;
        FOR(i, a, b+1){
            if(is_palin(i) && is_square(i) && is_palin(sqrt(i)) ){
                ct++;
            }
        }
        cout << "Case #" << tc << ": " << ct << endl;
    }
    return 0;
}