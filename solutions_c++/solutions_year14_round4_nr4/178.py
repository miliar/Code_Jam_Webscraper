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
#include <map>

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

int M; //strings
int N; //servers

struct TNode{
    LL V; // max vertices
    LL S; // max servers
    LL W; // ways
    map<char,int> next;
    bool leaf;
    TNode() : leaf(false){}
};

vector<TNode> trie;

void trieInit(){
    trie.resize(1);
    trie[0].next.clear();
    trie[0].leaf = false;
}

void trieAdd(char *p){
    int id = 0;
    for(; *p; p++){
        if (trie[id].next.find(*p) == trie[id].next.end()){
            trie[id].next[*p] = SIZE(trie);
            trie.PB(TNode());
        } 
        id = trie[id].next[*p];
    }
    trie[id].leaf = true;
}

void readTest(){
    scanf("%d%d",&M,&N);
    trieInit();
    char buf[200];
    REP(i,M){
        scanf("%s",buf);
        trieAdd(buf);
    }
}

#define MOD 1000000007

LL add(LL a,LL b){
    return ((a+b) % MOD);
}

LL mul(LL a, LL b){
    return ((a*b) % MOD);
}

LL lowFact(LL n, LL k){
    LL res = 1;
    REP(i,k) res = mul(res,n-i);
    return res;
}

LL binom[101][101];

void initBinom(){
    binom[0][0] = 1;
    for(int n = 1; n <= 100; n++){
        binom[n][0] = binom[n][n] = 1;
        for(int k=1; k < n; k++)
            binom[n][k] = add(binom[n-1][k-1],binom[n-1][k]);
    }
}

void solveNode(int id){
    //DB(id);
    trie[id].V = trie[id].S = 0;
    trie[id].W = 1;
    LL &V = trie[id].V;
    LL &S = trie[id].S;
    LL &W = trie[id].W;
    VI sz;
    for(const auto v : trie[id].next){
        V += trie[v.Y].V;
        S += trie[v.Y].S;
        W = mul(W,trie[v.Y].W);
        sz.PB(trie[v.Y].S);
    }
    if (trie[id].leaf){ 
        sz.PB(1);
        S++;
    }
    S = min(S,(LL)N);
    V += S;
    VC<LL> dyn(S+1,0); dyn[0] = 1;
    //print(dyn);
    for(auto s : sz){
        for(int i = S; i >= 0; i--){
            LL val = 0;
            for(int base = 0; base <= i ; base++){
                if (s-(i-base) < 0)
                    continue;
                val = add(val, mul(binom[S-base][i-base] , mul(binom[base][s-(i-base)] , dyn[base])));
            }     
            dyn[i] = val;
        }
        //print(dyn);
    }
    //DB(S); DB(W);
    //print(dyn);
    W = mul(W,dyn[S]);
    //DB(W);
}

void solveTrie(){
    for(int id = SIZE(trie)-1; id >= 0; id--)
        solveNode(id);
    // Now mul the 0-th W by N over S
}

void solveTest(int t){
    solveTrie();
    printf("Case #%d:",t);
    printf(" %lld %lld",trie[0].V,trie[0].W);
    printf("\n");
}

int main(int argc, char *argv[]){
    initBinom();
    int T;
    scanf("%d",&T);
    REP(t,T){
        readTest();
        solveTest(t+1);
    }
    return 0;
}
