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

using namespace std;

#define FOREACH(i, c) for(__typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for(__typeof(n) i = (a); i<(n); ++i)
#define REP(i, a, n) for(__typeof(n) i = (a); i<=(n); ++i)
#define ROF(i, n, a) for(__typeof(n) i = (n); i>=(a); --i)
#define error(n) cout << #n << " = " << n << endl
#define all(c) c.begin(), c.end()
#define pb push_back
#define po pop_back
#define Size(n) ((int)(n).size())
#define X first
#define Y second
#define scanf _ = scanf
// #define X real()
// #define Y imag()

typedef long long   ll ;
typedef long double ld ;
typedef pair<int,int> pii ;

const int maxn = 1111;

int T;

int n;
int a[maxn] , b[maxn],c[maxn];

int Inversion() {
    FOR (i,0,n) {
//         cerr << b[i] << " ";
        FOR (j,0,n)
        if (a[j] == b[i])
            c[j] = i;
    }
    int ans = 0;
    FOR (i,0,n)
        FOR (j,i+1,n)
        if (c[i] > c[j])
            ++ans;
    return ans;
}

int main() {
    cin >> T;
    REP (lv,1,T) {
        cin >> n;
        FOR (i,0,n) {
            cin >> a[i];
            b[i] = a[i];
        }
        sort (b,b+n);
        int ans = n*(n-1)/2;
        do{
            int id = 0;
            for (int i = 0 ; i < n ; ++i)
                if (b[i] > b[id])
                    id = i;
            bool flag = true;
            FOR (i,0,id-1)
                if (b[i] > b[i+1])
                    flag =false;
            FOR (i,id+1,n)
                if (b[i] > b[i-1])
                        flag = false;
              if (flag) {
                ans = min(ans,Inversion());
            }
        }while(next_permutation(b,b+n));
        cout << "Case #" << lv << ": " << ans << endl;
    }
    return 0 ;
}
