#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <fstream>
#include <set>

#define FOR(i,a,b)  for(__typeof(b) i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define FOREACH(x,c)   for(__typeof(c.begin()) x=c.begin();x != c.end(); x++)
#define ALL(c)      c.begin(),c.end()
#define CLEAR(c)    memset(c,0,sizeof(c))
#define SIZE(c) (int) ((c).size())

#define PB          push_back
#define MP          make_pair
#define X           first
#define Y           second

#define ULL         unsigned long long
#define LL          long long
#define LD          long double
#define II         pair<int, int>
#define DD         pair<double, double>

#define VC	    vector
#define VI          VC<int>
#define VVI         VC<VI>
#define VD          VC<double>
#define VS          VC<string>
#define VII         VC<II>
#define VDD         VC<DD>

#define DB(a)       cerr << #a << ": " << a << endl;

using namespace std;

template<class T> void print(VC < T > v) {cerr << "[";if (SIZE(v) != 0) cerr << v[0]; FOR(i, 1, SIZE(v)) cerr << "," << v[i]; cerr << "]\n";}
template<class T> string i2s(T &x) { ostringstream o; o << x; return o.str(); }
VS split(string &s, char c = ' ') {VS all; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) all.PB(s.substr(p, np - p)); p = np + 1;} if (p < SIZE(s)) all.PB(s.substr(p)); return all;}

int n;

void solve_case(int t){
    int R,C,M,A,W,E;
    cin >> R >> C >> M;
    A = R*C; W = min(R,C); E = A-M;
    VS board(R,string(C,'*'));
    int possible = 0;
    if (W == 1){
        possible = 1;
        if (R == 1)
            REP(i,E) board[0][i] = '.';
        else
            REP(i,E) board[i][0] = '.';
    } else if (E == 1)
        possible = 1;
    else if (W == 2){
        if (E%2 == 0 && E>2){
            possible = 1;
            if (R == 2)
                REP(i,E/2) board[0][i] = board[1][i] = '.';
            else
                REP(i,E/2) board[i][0] = board[i][1] = '.';
        }
    } else{
        if (E==4 || E==6){
            possible = 1;
            REP(i,E/2) board[0][i] = board[1][i] = '.';
        } else if (E==8){
            possible = 1;
            REP(i,3) board[0][i] = board[1][i] = '.';
            board[2][0] = board[2][1] = '.';
        }else if (E >= 9){
            possible = 1;
            int D = min(C,(E-2)/2);
            int r = 0;
            while (E > 0){
                int cols = min(D,E);
                REP(i,cols) board[r][i] = '.';
                E -= cols;
                r++;
            }
            if ((A-M) % D == 1){
                board[r-1][1] = '.';
                board[r-2][D-1] = '*';
            }
        }
    }
    board[0][0] = 'c';
    cout << "Case #" << t << ": " << endl;
    if (!possible){
        cout << "Impossible" << endl;
    }
    else
        FOREACH(s,board) cout << *s << endl;
}

int main(int argc, char *argv[]){
    cin >> n;
    REP(i,n)
        solve_case(i+1);    
    return 0;
}
