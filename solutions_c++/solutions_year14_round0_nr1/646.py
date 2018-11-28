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
    VVI b1(4,VI(4));
    VVI b2(4,VI(4));
    int a1, a2;
    cin >> a1;
    REP(x,4)REP(y,4) cin >> b1[x][y];
    cin >> a2;
    REP(x,4)REP(y,4) cin >> b2[x][y];
    int cnt = 0;
    int answer = -1;
    FOR(i,1,17) if (find(ALL(b1[a1-1]),i) != b1[a1-1].end() && find(ALL(b2[a2-1]),i) != b2[a2-1].end()){
        cnt++;
        answer = i;
    } 
    cout << "Case #" << t << ": ";
    if (cnt == 1)
        cout << answer;
    else if (cnt > 1)
        cout << "Bad magician!";
    else
        cout << "Volunteer cheated!";
    cout << endl;
}

int main(int argc, char *argv[]){
    cin >> n;
    REP(i,n)
        solve_case(i+1);    
    return 0;
}
