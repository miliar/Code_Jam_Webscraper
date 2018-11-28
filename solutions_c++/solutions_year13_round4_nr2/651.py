/*==================================================*\
 | Author: ziki
 | Created Time: 2013/6/1 22:38:59
 | File Name: B.cpp
 | Description: 
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
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;
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

int stk[100];
int main() {
    int T;
    cin>>T;
    rep(cas,T) {
        int64 a,b, ans2;
        cin>>a>>b;
        printf("Case #%d: ",cas+1);
        int d = 0;
        int64 tmp = b;
        rep(i,a) {
            stk[i] = tmp%2; tmp/=2;
        }
        ans2 = 0;
        int64 ans1 = 0,man = 0, pos = 1;
        //cout<<a<<' '<<b<<endl;
        int64 tot = (1LL<<a);
        for(int i=0; i<a; i++) {
            man += 1<<i;
            if(pos<=b) {
                ans1 = man-1;
                //checkmax(ans1, man-1);
            }
            //cout<<man<<' '<<pos<<endl;
            pos += 1ll<<(a-i-1);
        }
        if(b == (1ll<<a)) ans1 = (1ll<<a)-1;
        man = tot; int64 cnt = 0;
        for(pos = tot; pos > 0; pos = pos /2) {
            int64 now = man - cnt -1;
            //out(now);
            if(pos <= b) {
                ans2 = now; break;
            }
            cnt=cnt*2+1;
        }
        if( b == 1 ) ans2 = 0;
        cout<<ans1<<' '<<ans2<<endl;
        //cout<<ans2<<endl;
    }
	return 0;
}

