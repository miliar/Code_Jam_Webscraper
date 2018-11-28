#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <cassert>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>

using namespace std;

#define LL long long
#define F first
#define S second
#define PB push_back
#define PF push front
#define MP make_pair
#define REP(x, n) for(int x=0; x<(n); ++x)
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define VAR(v,n) __typeof(n) v=(n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define MOD(x, n) ((x)%(n)+(n))%(n)
#define SZ(x) (int((x).size()))
#define ALL(x) ((x).begin()),((x).end())
#define SORT(v) sort((v).begin(),(v).end())
#define UNIQUE(v) SORT(v),(v).erase(unique((v).begin(),(v).end()),(v).end())
LL GCD( LL a , LL b ) { while( b ) b ^= a ^= b ^= a %= b ; return a ; }
LL LCM( LL a , LL b ) { return a * ( b / GCD( a , b ) ) ; }

typedef vector<int>    VI;
typedef vector<VI>     VVI;
typedef vector<LL>     VLL;
typedef vector<bool>   VB;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII>    VPII;
typedef pair<LL, LL>   PLL;
typedef vector<PLL>    VPLL;

typedef list<int>       LI;

const double EPS = 10e-9;
const double INF = (1LL << 30);

using namespace std;

std::string int2str( int n )
{
    std::ostringstream result;
    result << n;
    return result.str();
}

int str2int( const std::string& s )
{
    int result;
    std::istringstream ss( s );
    ss >> result;
    if (!ss) throw std::invalid_argument( "StrToInt" );
    return result;
}

void pr(int i, string res) {
    cout << "Case #" << i << ": " << res << endl;
}

void solve(int irun, VS &m) {
    bool noEmpty = false;

    int x,y;
    bool t;

    // horizontal
    REP(i, SZ(m)) {
        x=0,y=0;t=false;
        REP(j,SZ(m[i])) {
            char c = m[i][j];
            if (c == 'O')       y++;
            else if (c=='X')    x++;
            else if (c=='T')    t=true;
            else                noEmpty = true;
        }
        if (y==3 && t || y==4) {
            pr(irun, "O won");
            return;
        } else if (x==3 && t || x==4) {
            pr(irun, "X won");
            return;
        }
    }


    // vertical
    REP(i, SZ(m)) {
        x=0,y=0;t=false;
        REP(j,SZ(m[i])) {
            char c = m[j][i];
            if (c == 'O')       y++;
            else if (c=='X')    x++;
            else if (c=='T')    t=true;
            else                noEmpty = true;
        }
        if (y==3 && t || y==4) {
            pr(irun, "O won");
            return;
        } else if (x==3 && t || x==4) {
            pr(irun, "X won");
            return;
        }
    }

    x=0,y=0;
    t=false;
    // diagonal 1
    REP(i,SZ(m)) {
        char c = m[i][i];
        if (c == 'O')       y++;
        else if (c=='X')    x++;
        else if (c=='T')    t=true;
        else                noEmpty = true;
        
    }
    if (y==3 && t || y==4) {
        pr(irun, "O won");
        return;
    } else if (x==3 && t || x==4) {
        pr(irun, "X won");
        return;
    }

    x=0,y=0;
    t=false;
    // diagonal 2
    REP(i,SZ(m)) {
        char c = m[SZ(m)-i-1][i];
        if (c == 'O')       y++;
        else if (c=='X')    x++;
        else if (c=='T')    t=true;
        else                noEmpty = true;
        
    }
    if (y==3 && t || y==4) {
        pr(irun, "O won");
        return;
    } else if (x==3 && t || x==4) {
        pr(irun, "X won");
        return;
    }

    if (noEmpty)
        pr(irun, "Game has not completed");
    else
        pr(irun, "Draw");


}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int N;
    cin >> N;
    string c;
    VS matr(4, "");
    REP(i,N) {
        REP(j,4) {
            cin >> c;
            matr[j] = c;
//            cout << "line: " << c << endl;
        }
        solve(i+1, matr);
    }
    return 0;
}    
