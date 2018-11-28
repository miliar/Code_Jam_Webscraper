#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef map<int, int> MI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<vector<int> > VVI;
typedef vector<vector<LL> > VVL;
const double pi=acos(-1.0);
const double eps=1e-11;
const int mod = 1e7 + 9;
const int oo = (1 << 31) - 1;

#define two(X) (1<<(X))
#define twoL(X) ((1LL)<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

#define rep(i, n) rb(i, 0, n)
#define rb(i, b, n) rbc(i, b, n, <)
#define rbe(i, b, n) rbc(i, b, n, <=)
#define rbc(i, b, n, c) for(int i = ((int)(b)); i c ((int)(n)); i++)

#define p(x) cout << x;
#define ps(x) cout << x << " "
#define pl cout << endl
#define pn(x) cout << x << endl

#define s(v) ((int) v.size())
#define all(v) v.begin(), v.end()
#define MP make_pair
#define PB push_back
#define X first
#define Y second
#define getcx getchar
//_unlocked

template<class T>
inline void readInt( T &n )//fast input function
{
   n=0;
   T ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   n=n*sign;
}
/**************************************************/

int win(vector<string> b) {
    int x, o, t;

    x = o = t = 0;
    rep(i, 4)
        if(b[i][i] == 'X') x++;
        else
        if(b[i][i] == 'O') o++;
        else
        if(b[i][i] == 'T') t++;

    if(x == 4 || (x == 3 && t == 1)) return 0;
    if(o == 4 || (o == 3 && t == 1)) return 1;

    x = o = t = 0;
    rep(i, 4)
        if(b[i][4 - i - 1] == 'X') x++;
        else
        if(b[i][4 - i - 1] == 'O') o++;
        else
        if(b[i][4 - i - 1] == 'T') t++;

    if(x == 4 || (x == 3 && t == 1)) return 0;
    if(o == 4 || (o == 3 && t == 1)) return 1;

    rep(i, 4) {
        x = o = t = 0;
        rep(j, 4)
            if(b[i][j] == 'X') x++;
            else
            if(b[i][j] == 'O') o++;
            else
            if(b[i][j] == 'T') t++;

        if(x == 4 || (x == 3 && t == 1)) return 0;
        if(o == 4 || (o == 3 && t == 1)) return 1;
    }


    rep(i, 4) {
        x = o = t = 0;
        rep(j, 4)
            if(b[j][i] == 'X') x++;
            else
            if(b[j][i] == 'O') o++;
            else
            if(b[j][i] == 'T') t++;

        if(x == 4 || (x == 3 && t == 1)) return 0;
        if(o == 4 || (o == 3 && t == 1)) return 1;
    }

    return -1;
}

bool draw(vector<string> b) {
    rep(i, 4) rep(j, 4)
        if(b[i][j] == '.') return false;
    return true;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int TC = 1, T;
    char* res;
    vector<string> b(4);

    for(scanf("%d", &T); TC <= T; TC++) {
        //scanf("%d", &n);

        rep(i, 4) cin >> b[i];

        int w = win(b);
        if(w == -1) {
            if(draw(b)) res = "Draw";
            else res = "Game has not completed";
        }
        else
        if(!w) res = "X won";
        else res = "O won";

        printf("Case #%d: %s\n", TC, res);
    }

    return 0;
}



