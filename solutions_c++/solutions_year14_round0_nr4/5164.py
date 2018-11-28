/*
http://codingaquarium.wordpress.com/
Shaikh shiam Rahman
Khunla University of Engineering and Technology(KUET)

*/

#include <bits/stdc++.h>
using namespace std;

/*** typedef ***/

#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define stream istringstream
#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define repl(i,n) for(__typeof(n) i=1; i<=(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define INF (1<<30)
#define PI acos(-1.0)
#define pb push_back
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x))
#define memsp(x) mem(x,MEMSET_INF)
#define memdp(x) mem(x,-1)
#define memca(x) mem(x,0)
#define eps 1e-9
#define ii pair<int,int>
#define pmp make_pair
#define ft first
#define sd second
#define vi vector<int>
#define vii vector<ii>
#define si set<int>
#define msi map<string , int >
#define mis map<int , string >
typedef long long i64;
typedef unsigned long long ui64;

/** function **/

#define SDi(x) sf("%d",&x)
#define SDl(x) sf("%lld",&x)
#define SDs(x) sf("%s",x)
#define SD2(x,y) sf("%d%d",&x,&y)
#define SD3(x,y,z) sf("%d%d%d",&x,&y,&z)
#define pf printf
#define sf scanf
#define pfcas(x) pf("Case %d: ",x)

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define MAX 20010

int main (int argc, char **argv) {
#ifndef ONLINE_JUDGE
    READ("input.txt");
    WRITE("out.txt");
#endif
    int tc,N,wi,cas=0,y,z,yy;
    double w;
    priority_queue< int,vector<int>,greater<int> > n,k;
    priority_queue< int > dn,dk;
    SDi(tc);
    while(tc--){
        SDi(N);
        rep(i,N){
            sf("%lf",&w);
            wi = (w+0.00000001)*1000000;
            n.push(wi);
            dn.push(wi);
        }
        rep(i,N){
            sf("%lf",&w);
            wi = (w+0.00000001)*1000000;
            k.push(wi);
            dk.push(wi);
        }

        while(k.size()){
            while(k.top()<n.top() and k.size())
                k.pop();
            if(k.size())
                k.pop(),n.pop();
        }
        z = n.size();
        yy = 0;
        while(dk.size()){
            while(dn.top()<dk.top() and dk.size())
                dk.pop();
            if(dk.size())
                dn.pop(),dk.pop(),yy++;
        }
        y = yy;
        pf("Case #%d: %d %d\n",++cas,y,z);

        n   = priority_queue< int,vector<int>,greater<int> >();
        k   = priority_queue< int,vector<int>,greater<int> >();
        dn  = priority_queue< int >();
        dk  = priority_queue< int >();
    }
    return 0;
}
