#include <vector>
#include <iostream>
#include <unordered_map>
#include <map>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <cassert>
#include <cmath>
using namespace std;

#ifndef MDEBUG
#define NDEBUG
#endif

#define x first
#define y second
#define ll long long
#define d double
#define ld long double
#define pii pair<int,int>
#define pil pair<int,ll>
#define pli pair<ll,int>
#define pll pair<ll,ll>
#define pss pair<string,string>
#define psi pair<string,int>
#define pis pair<int,string>
#define psl pair<string,ll>
#define pls pair<ll,string>
#define wh(x) (x).begin(),(x).end()
#define ri(x) int x;cin>>x;
#define rii(x,y) int x,y;cin>>x>>y;
#define rl(x) ll x;cin>>x;
#define rv(v) for(auto&_cinv:v) cin>>_cinv;
#define wv(v) for(auto&_coutv:v) cout << _coutv << ' '; cout << endl;
#define ev(v) for(auto&_cerrv:v) cerr << _cerrv << ' '; cerr << endl;
#define MOD 1000000007

namespace std { 
template<typename T,typename U>struct hash<pair<T,U>>{hash<T>t;hash<U>u;size_t operator()(const pair<T,U>&p)const{return t(p.x)^(u(p.y)<<7);}};
}
// auto fraclt = [](auto&a,auto&b) { return (ll)a.x * b.y < (ll)b.x * a.y; };
template<typename T,typename F>T bsh(T l,T h,const F&f){T r=-1,m;while(l<=h){m=(l+h)/2;if(f(m)){l=m+1;r=m;}else{h=m-1;}}return r;}
template<typename T,typename F>T bsl(T l,T h,const F&f){T r=-1,m;while(l<=h){m=(l+h)/2;if(f(m)){h=m-1;r=m;}else{l=m+1;}}return r;}
template<typename T> T gcd(T a,T b) { if (a<b) swap(a,b); return b?gcd(b,a%b):a; }
template<typename T> void fracn(pair<T,T>&a) {auto g=gcd(a.x,a.y);a.x/=g;a.y/=g;}
template<typename T> struct Index { int operator[](const T&t){auto i=m.find(t);return i!=m.end()?i->y:m[t]=m.size();}int s(){return m.size();} unordered_map<T,int> m; };

struct ast { ll x,y,z; int vx,vy,vz; };

int main(int,char**) {
    ri(T)
    for (int t=1;t<=T;++t) {
        cout << "Case #" << t << ": ";
        rii(N,S);
        vector<ast> A(N);
        vector<ll> B(N);
        vector<bool> C(N,false);
        for (ast & a:A) {
            cin >> a.x >> a.y >> a.z >> a.vx >> a.vy >> a.vz;
        }

        for (int i = 0; i < N; i++) {
            B[i] = 1LL << 62;
        }

        B[0] = 0.0;
        while(true) {
            ll best=1LL << 62; int j = -1;
            for (int i = 0; i < N; i++) {
                if (!C[i] && B[i] < best) { best = B[i]; j = i; }
            }
            if (j == 1) break;
    
            C[j] = true;
            for (int i = 0; i < N; ++i) {
                B[i] = min(B[i], max(B[j], (A[i].x-A[j].x)*(A[i].x-A[j].x)+(A[i].y-A[j].y)*(A[i].y-A[j].y)+(A[i].z-A[j].z)*(A[i].z-A[j].z)));
            }

        }
        // ev(B);
        printf("%.015f\n",  sqrt(B[1]));
        

    }
}

