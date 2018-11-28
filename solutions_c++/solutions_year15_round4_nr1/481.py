/*
AUTHOR : VUAcoder
LANGUAGE : C++
PROBLEM :
*/

#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<set>
#include<fstream>
#include<cfloat>
using namespace std;
#define PI (2.*acos(0.))
#define EPS 1e-9
#define ZERO(x)     (fabs(x) < EPS)
#define EQ(a,b)     (ZERO((a)-(b)))
#define LESSER(a,b) (!EQ(a,b) && (a)<(b))
#define GREATER(a,b)(!EQ(a,b) && (a)>(b))
#define GETBIT(x,i) (x&(1<<i))
#define SETBIT(x,i) (x|(1<<i))
#define FORab(i,a,b) for(typeof(b) i=(a);i<=(b);i++)
#define FOR(i,n) FORab(i,0,(n)-1)
#define FOR1(i,n) FORab(i,1,n)
#define FORit(it,a) for( typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define all(a) (a).begin(),(a).end()
#define ms(a,b) memset((a),(b),sizeof(a))
#define pb push_back
#define sz(a) (int)a.size()
#define in(a,b,c) ((a) <= (b) && (b) <= (c))
#define px first
#define py second
#define __eXYZ__
#ifdef __eXYZ__
//USE THESE FOR DEBUG
#define RFILE(a)    freopen(a, "r", stdin)
#define WFILE(a)    freopen(a, "w", stdout)
#define _r(arg) {dbg,arg; dbg.start(); }
#define _n(arg...) {_r(#arg " ==> ");dbg,arg; }
#define _(arg...) { _n(arg); dbg.nl(); }
#else
#define RFILE(a)
#define WFILE(a)
#define _n(arg) {}
#define _n(arg...) {}
#define _(arg...) {}
#endif


typedef long long  LL;
typedef vector<int>   vi;
typedef pair<int,int>  pii;

template<class A, class B> ostream &operator<<(ostream& o, pair<A,B>& p) { //pair print
    return o << "("<<p.first<<", "<<p.second<<")";
}

template<class T> ostream& operator<<(ostream& o, const vector<T>& v) { //vector print
    o << "{";FORit(it, v) o << *it << ", "; return o << "}";
}

struct debugger
{
    ostream &out; bool first;
    void start() { first = true; }
    debugger(ostream& out):out(out) {start();}
    void nl() { out << endl; start(); }
    // Taken from rudradevbasak
    template<class T> debugger& operator,(T& v) {
        if(first) first = false; else out << ", ";
        out << v; return *this;
    }
    template<class T> debugger& operator,(pair<T*,int> arr) { //array print
        out << "{";
            FOR(i, arr.second) { out << arr.first[i] << ", "; }
        out << "}";
        return *this;
    }
} dbg(cerr);

string grid[222];
int r,c;
bool bad(int x, int y,char cc){
    int dr,dc;
    if(cc =='<' ) dr = 0, dc=-1;
    if(cc =='>' ) dr = 0, dc=1;
    if(cc =='^' ) dr = -1, dc=0;
    if(cc =='v' ) dr = 1, dc=0;
    //cerr<<"HERE"<<x<<" "<<y<<" "<<dr<<" "<<dc<<endl;
    do{
        x+=dr;
        y+=dc;

        if(x <0 || y< 0 || x>=r ||y>=c)return true;
    }while(grid[x][y]=='.');
    return false;
}

int row[222];
int col[222];
int main()
{
    RFILE("input.txt");
    WFILE("output_r2_a_large.txt");
    int t, cn=1;
    cin>>t;
    while(t--){
        cin>>r>>c;
        FOR(i,r)
            cin>>grid[i];
            int ans=0;
    ms(row,0);
    ms(col,0);
        FOR(i,r)
            FOR(j,c){
                if(grid[i][j] != '.'){
                    row[i]++;
                    col[j]++;
                   // cerr<<"HERE"<<i<<" "<<j<<endl;
                    if(bad(i,j,grid[i][j])){
                          //  cerr<<"BAD"<<endl;
                        ans++;
                    }
                }
            }
            int ok=true;
        FOR(i,r)
            FOR(j,c){
                if(grid[i][j] != '.'){
                    if(bad(i,j,grid[i][j])){
                        if(row[i] > 1 || col[j]> 1) continue;
                        else ok =false;
                    }
                }
            }
            if(!ok)cout<<"Case #"<<cn++<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<cn++<<": "<<ans<<endl;
    }
    return 0;
}

