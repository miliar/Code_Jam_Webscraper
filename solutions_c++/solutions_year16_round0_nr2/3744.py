#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()
#define sz(s) ((int) ((s).size()))
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornr(i, n) for (int i = (int)(n)-1; i>=0; --i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define for1r(i, n) for (int i = (int)(n); i>0; --i)

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;

int mod1 = int(1e9) + 7;

#define MX 100100


void main2(){

    vi neg = vi(110,INT_MAX), pos = vi(110,INT_MAX);

    neg[0] = pos[0] = 0;

    string s;
    cin >> s;

    int sl = s.length();

    for1(i,sl) {
        if(s[i-1] == '+') {
            pos[i] = min(pos[i], pos[i-1]);
            pos[i] = min(pos[i], neg[i-1] + 2);
            neg[i] = min(neg[i], pos[i-1] + 1);
        } else {
            neg[i] = min(neg[i], neg[i-1]);
            neg[i] = min(neg[i], pos[i-1] + 2);
            pos[i] = min(pos[i], neg[i-1] + 1);
        }
    }

    cout << pos[sl] << endl;

}


int main(){

    int t;
    ri(t);

    for1(cas,t) {
        printf("Case #%d: ", cas);
        main2();
    }

    return 0;
}
