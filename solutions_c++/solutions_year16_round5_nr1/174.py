#include <vector>
#include <iostream>
#include <unordered_map>
#include <map>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <cassert>
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

int main(int,char**) {
    ri(T)

    int ** F = new int*[4];
    for (int i =0;i<4;++i) {
        F[i] = new int[20001]();
    }
    for (int t=1;t<=T;++t) {
        cout << "Case #" << t << ": ";
        string S;
        cin >> S;
        int N = S.size();
        for (int i=0;i<4;++i) {
            for (int j = 0; j < N+1; j++) {
                F[i][j] = -1;
            }

        }
        F[0][0] = F[1][0] = 0;

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j <= i; ++j) {
                for (int k = 0; k < 2; ++k) {
                    if (F[k][j] == -1) continue;
                    if (j > 0 && ((k ^ (j&1)) ^ (S[i] == 'C'))) {
                        F[k+2][j-1] = max(F[k+2][j-1], 10 + F[k][j]);
                    } else if (j>0) {
                        F[k+2][j-1] = max(F[k+2][j-1], 5 + F[k][j]);
                        F[k+2][j+1] = max(F[k+2][j+1], F[k][j]);
                    } else if (k ^ (S[i] == 'J')) {
                        F[k+2][j+1] = max(F[k+2][j+1], F[k][j]);
                    }
                }
            }

            swap(F[0],F[2]); swap(F[1],F[3]);
            for (int j = 0; j <= N; ++j) {
                //cout << F[0][j] << ' ' << F[1][j] << endl;
                F[2][j] = F[3][j] = -1;
            }
            //cout << endl;

            F[0][0] = F[1][0] = max(F[0][0],F[1][0]);
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            ans = max(ans, F[0][i]);
            ans = max(ans, F[1][i]);
        }
        cout << ans << endl;
    }
}

