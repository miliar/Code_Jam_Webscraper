#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <climits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

#define FORT for(int t=1;t<=T;t++)
#define REP(x,s,n) for(int x=s; x<n; x++)
#define EPSILON (1E-6)
#define CODEJAM 0
#define MAXN 131073
#define sz(s) (s).size()
#define pb(s) push_back((s))
#define all(s) (s).begin(),(s).end()

using namespace std;

typedef long int LI;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mii;

bool CompareDouble(const LD &, const LD &);

int main() {
    freopen("qualA-large.in", "r+", stdin);
    freopen("outputA.txt", "w+", stdout);
    int T;
    cin >> T;
    FORT {
         int smax, res = 0, total = 0;
         string s;
         cin >> smax >> s;
         REP (i,0,sz(s)) {
             if (total < i) {
                res++;
                total++;
             }
             total = total + (s[i]-48);
         }
         printf("Case #%d: %d\n", t, res);
    }
    return 0;
}

bool CompareDouble(const LD &a, const LD &b) {
    return fabs(a - b) < EPSILON;
}
