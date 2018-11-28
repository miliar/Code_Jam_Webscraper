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
#define VLL     VC<LL>

#define DB(a)       cerr << #a << ": " << a << endl;

using namespace std;

template<class T> void print(VC < T > v) {cerr << "[";if (SIZE(v) != 0) cerr << v[0]; FOR(i, 1, SIZE(v)) cerr << "," << v[i]; cerr << "]\n";}
template<class T> string i2s(T &x) { ostringstream o; o << x; return o.str(); }
VS split(string &s, char c = ' ') {VS all; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) all.PB(s.substr(p, np - p)); p = np + 1;} if (p < SIZE(s)) all.PB(s.substr(p)); return all;}

int n;
LL p,q,r,s;
LL sum;
VLL T;

void readTest(){
    scanf("%d %lld %lld %lld %lld",&n, &p, &q, &r, &s);
    T.resize(n);
    REP(i,n)
        T[i] = (i * p + q) % r + s;
    sum = 0;
    REP(i,n)
        sum += T[i];
}

void solveTest(int t){
    double res;
    
    LL s1=0, s2=T[0], s3=sum-T[0];
    LL best = max(s2,s3);
    int i=0, j=0;
    LL score = -1;
    while(1){
        if (s3 >= best){
            j++;
            if (j == n)
                break;
            s2 += T[j];
            s3 -= T[j];
        } else if (s2 >= best){
            i++;
            s1 += T[i-1];
            if (s1 >= best)
                break;
            s2 -= T[i-1];
        } else if (s1 >= best)
            break;
        score = max(s1,max(s2,s3));
        if (score < best)
            best = score;
    }
    res = 1- ((double)best)/sum;
    printf("Case #%d:",t);
    printf(" %.11g",res);
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
