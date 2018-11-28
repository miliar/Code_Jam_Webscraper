#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <ctime>

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
using namespace std;
typedef vector<int> vi;
typedef map<int,int> mii;
typedef long long ll;
template <class T> void checkmax(T &t, T x){if (x > t) t = x;}
template <class T> void checkmin(T &t, T x){if (x < t) t = x;}
template <class T> void _checkmax(T &t, T x){if (t == -1 || x > t) t = x;}
template <class T> void _checkmin(T &t, T x){if (t == -1 || x < t) t = x;}
#define INF (INT_MAX/10)
#define SQR(x) ((x)*(x))
#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define iter(v) __typeof((v).begin())
#define foreach(it, v) for (iter(v) it = (v).begin(); it != (v).end(); it++)
#define clr(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define sz(a) ((int)(a).size())
#define all(a) a.begin(), a.end()
#define mid(x, y) ((x+y)/2)
#define vp vector<P>
#define M 1000

struct P{
    int t, x, p;
    P(int t, int x, int p):t(t),x(x),p(p){}
    bool operator <(const P&p)const{ 
        if (x!=p.x) return x<p.x; 
        return t<p.t;
    }
};

int i,j,k,m,n,l,x,y,p;
vector<P> a;

ll g(int n, int i){ return i*(2*n-i+1)/2; }

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    repf(test, 1, tests){
        scanf("%d%d", &n, &m);
        a.clear();
        ll ret=0, ret2=0;        
        repf(i, 1, m){
            scanf("%d%d%d", &x, &y, &p);
            ret2+=g(n, y-x)*p;
            a.pb(P(0, x, p));
            a.pb(P(1, y, p));
        }
        sort(all(a));
        stack<P> s;
        
        rep(i, sz(a))     
            if (a[i].t==0) s.push(a[i]);
            else{
                while (a[i].p){
                    k=min(a[i].p, s.top().p);
                    ret+=g(n, a[i].x-s.top().x)*k;
                    a[i].p-=k;
                    s.top().p-=k;
                    if (s.top().p==0) s.pop();
                }
            }
        printf("Case #%d: %d\n", test, ret2-ret);
    }
    return 0;
}
