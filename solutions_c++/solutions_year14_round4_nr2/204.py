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
VI T;

void readTest(){
    scanf("%d",&n);
    T.resize(n);
    REP(i,n) scanf("%d",&(T[i]));
}

int swaps(VI &X){
    int ret = 0;
    REP(i,SIZE(X))
        FOR(j,i+1,SIZE(X))
            if (X[i] > X[j])
                ret++;
    return ret;
}

int trySet(int i){
    VI a, b, c;
    REP(k,n){
        if (i%2){
            c.PB(0);
            a.PB(T[k]);
        }else{
            c.PB(1);
            b.PB(T[k]);
        }
        i /= 2;
    }
    reverse(ALL(b));
    return (swaps(a)+swaps(b)+swaps(c));
}

void solveTest(int t){
    int res = n*n;
    REP(i,(1 << n))
        res = min(res,trySet(i));
    printf("Case #%d:",t);
    printf(" %d",res);
    printf("\n");
}

int main(int argc, char *argv[]){
    int T;
    scanf("%d",&T);
    REP(t,T){
        readTest();
        solveTest(t+1);
    }
    return 0;
}
