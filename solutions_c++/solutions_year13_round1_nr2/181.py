/*==================================================*\
 |Author: ziki
 |Created Time: 2013/4/27 10:09:16
 |File Name: B.cpp
 |Description: 
\*==================================================*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>

using namespace std;
using namespace rel_ops;

typedef long long int64;
typedef unsigned long long uint64;
const double pi=acos(-1.0);
const double eps=1e-11;
const int inf=0x7FFFFFFF;
template<class T> inline bool checkmin(T &a,T b){return b<a?a=b,1:0;}
template<class T> inline bool checkmax(T &a,T b){return b>a?a=b,1:0;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define mem(a,b) memset(a, b, sizeof(a))
#define clr(a) memset(a, 0, sizeof(a))
#define rep(i,n) for(int i=0; i<n; i++)
#define repit(i,v) for(typeof(v.begin()) i=v.begin(); i!=v.end(); i++)
#define iter(v) typeof(v.begin())
#define ff first
#define ss second
#define out(x) (cout<<#x<<": "<<x<<endl)
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

const int N = 1e4+10;
int a[N];
int nxt[N];
int stk[N], sz;
int main() {
    int T;
    cin>>T;
    rep(cas,T) {
        int E,R,n;
        cin>>E>>R>>n;
        rep(i,n) cin>>a[i];
        sz = 0;
        rep(i,n) {
            while(sz>0 && a[stk[sz]] <= a[i]) {
                nxt[stk[sz--]] = i;
            }
            stk[++sz] = i;
        }
        while(sz>0) nxt[stk[sz--]] = -1;
        int64 ans = 0, now = E;
        rep(i,n) {
            if(nxt[i]==-1) {
                ans += now*a[i];
                now = 0;
            }
            else {
                int64 add = nxt[i]-i;
                int64 tot = add*R + now;
                if(tot>E) {
                    int64 del = min(tot-E,now);
                    ans += del*a[i];
                    now-=del;
                }
            }
            now += R;
            //cout<<now<<' '<<E<<endl;;
            if(now>=E) now = E;
        }
        printf("Case #%d: %lld\n",cas+1,ans);
        //show(a,n);
        //show(nxt,n);
    }
	return 0;
}

