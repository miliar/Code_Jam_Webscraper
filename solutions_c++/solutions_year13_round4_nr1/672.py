/*==================================================*\
 | Author: ziki
 | Created Time: 2013/6/1 23:50:31
 | File Name: A.cpp
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


int mod = 1000002013;
typedef int modtype;

struct Int{
    modtype x;
    Int ():x(0){}
    Int (const int &t):x(t%mod){}
    Int (const long long &t):x(t%mod){}
    Int (const Int &t):x(t.x){}
    Int operator + (const Int & b) const {
        return Int(x+b.x);
    }
    Int operator * (const Int & b) const {
        return Int((long long)x*b.x);
    }
    Int operator - (const Int & b) const {
        return Int((x-b.x)%mod+mod);
    }
    Int operator / (const Int & b) const {
        return *this * (b^(mod-2));
    }
    Int operator ^ (long long k) const {
        Int y = *this, ret = Int(1);
        while(k) {
            if(k&1) ret = ret*y;
            y = y*y;
            k>>=1;
        }
        return ret;
    }
    friend istream & operator>>(istream&,const Int&);
    friend ostream & operator<<(ostream&,const Int&);
};
ostream & operator<<(ostream& out, const Int& b) {
    out<<b.x;
    return out;
}
istream & operator>>(istream& in,  const Int& b) {
    in>>b.x;
    return in;
}

const int M = 10005;
int d[M];
int st[M], end[M], pas[M];
int64 flow[M];
int n,m;
Int cal(int64 dis) {
    if(dis == 0) return Int(0);
    int64 dd = dis, nn = n;
    int64 cal = dd*(nn + nn - dis+1)/2;
    return Int(cal);
}
int main() {
    int T; cin>>T;
    rep(cas,T) {
        int cnt = 0;
        scanf("%d%d",&n,&m);
        Int get = 0;
        rep(i,m) {
            scanf("%d%d%d",st+i, end+i, pas+i);
            d[cnt++] = st[i];
            d[cnt++] = end[i];
            get = get + cal(end[i] - st[i]) * Int(pas[i]);
        }
        //cout<<get<<endl;
        sort(d,d+cnt);
        cnt = unique(d,d+cnt) - d;
        //clr(flow);
        rep(i,m) {
            int l = lower_bound(d,d+cnt,st[i]) - d, r = lower_bound(d,d+cnt,end[i]) - d;
            for(int j=l+1;j<=r; j++) {
                flow[j] = flow[j] + pas[i];
            }
        }
        Int ans=0;
        rep(i,cnt) {
            while(flow[i]>0) {
                int j;
                for(j=i; j+1<cnt && flow[j+1]>0; j++);
                //out(j);
                int64 mx = 1ll<<60;
                long long dis = 0;
                for(int k=i; k<=j; k++) if(mx>flow[k]) mx = flow[k];
                for(int k=i; k<=j; k++) dis = dis + d[k] - d[k-1];
                ans = ans + cal(dis)*Int(mx);
                for(int k=i; k<=j; k++)  flow[k] -= mx;
                //show(flow,cnt);
            }
        }
        printf("Case #%d: ",cas+1);
        cout<<get-ans<<endl;
    }
	return 0;
}

