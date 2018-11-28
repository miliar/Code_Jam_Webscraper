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

int pw, tw,n;
VI gold;
VI hp;

void readTest(){
    scanf("%d %d %d",&pw,&tw,&n);
    gold.resize(n);
    hp.resize(n);
    REP(i,n) scanf("%d %d", &(hp[i]), &(gold[i]));
}

#define ADV_MAX 2000
#define INFTY 1000000000

int winAdv(int h){
    int res = (h-1)/tw;
    h -= tw*res;
    res -= (h+pw-1)/pw;
    return res;
}

int loseAdv(int h){
    return ( (h+tw-1)/tw );
}

void solveTest(int t){
    VC<LL> dp(ADV_MAX,-INFTY);
    VC<LL> dp2(dp);
    dp[1] = 0LL;
    REP(i,n){
        int win = winAdv(hp[i]);
        int lose = loseAdv(hp[i]);
        //DB(win); DB(lose);
        REP(j,ADV_MAX){
            LL v1 = -INFTY, v2 = -INFTY;
            if (j-win>=0 && j-win < ADV_MAX) 
                v1 = dp[j-win]+gold[i];
            if (j-lose>=0 && j-lose < ADV_MAX)
                v2 = dp[j-lose];
            dp2[j] = max(v1,v2);       
        }
        swap(dp2,dp);
        //print(dp);
    }
    LL res = 0;
    REP(i,SIZE(dp))
        res = max(res,dp[i]);
    printf("Case #%d:",t);
    printf(" %lld",res);
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
