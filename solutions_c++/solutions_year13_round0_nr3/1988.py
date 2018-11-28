#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <cmath>
#include <list>
#include <vector>
#include <iomanip>
#include <cctype>
#include <complex>
#include <iterator>
#include <ostream>
#include <bitset>
#define all(a) a.begin(),a.end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define clx complex<long double>
typedef long long ll;
typedef long double ldb;
typedef unsigned long long ull;

using namespace std;
int _bufint;
inline int in(){
    scanf("%d", &_bufint);
    return _bufint;
}
const ll LINF=~((1ll)<<63);
const int INF=~(1<<31);
struct pl{
    ll x,y,z;
    ll dx,dy,dz;
    ll nx, ny, nz;
    ll left, right;
    pl(int xx, int yy, int zz, int dxx, int dyy, int dzz){
        x=xx;
        y=yy;
        z=zz;
        dx=dxx;
        dy=dyy;
        dz=dzz;
        nx=x;
        ny=y;
        nz=z;
        left=-1, right=-1;
    }
    void step(int n){
        nx=x+dx*n;
        ny=y+dy*n;
        nz=z+dz*n;
    }
    ull dist(){
        return (ull)(nx*nx)+ull(ny*ny)+ull(nz*nz);
    }
};
/*
struct node{
    vector<int> cur;
    node(int a){
        cur.pb(a);
    }
    node(){
    }
};
const int maxn=1000000*4+100;
node tree[maxn];
node merge(node a, node b){
    node c;
    c.cur.assign(a.cur.size()+b.cur.size(),0);
    merge(a.cur.begin(), a.cur.end(), b.cur.begin(), b.cur.end(), c.cur.begin());
    return c;
}
int query(int v, int tl, int tr, int l, int r, int cr){
    if(l>r) return 0;
    if(tr==r && tl==l){
        return (upper_bound(tree[v].cur.begin(), tree[v].cur.end(), cr) - tree[v].cur.begin() - 1);
    }
    int tm=tl+(tr-tl)/2;
    return query(2*v, tl, tm, l, min(r, tm), cr) + query(2*v+1, tm+1, tr, max(l, tm+1), r, cr);
}
*/
ll toll(string a){
    ll res=0;
    for(int i=0;i<a.size();++i){
        res*=10;

        res+=a[i]-'0';
    }
    for(int i=a.size()-1;i>=0;--i){
        res*=10;

        res+=a[i]-'0';
    }
    return res*res;
}
ll toll2(string a, int k){
    ll res=0;
    for(int i=0;i<a.size();++i){
        res*=10;

        res+=a[i]-'0';
    }
    res*=10;
    res+=k;
    for(int i=a.size()-1;i>=0;--i){
        res*=10;

        res+=a[i]-'0';
    }
    return res*res;
}
string tostr(ll a){
    string res="";
    while(a){
        res.pb(a%10+'0');
        a/=10;
    }
    reverse(res.begin(), res.end());
    return res;
}
bool ispal(string s){
    for(int i=0;i<s.size()/2;++i){
        if(s[i]!=s[s.size()-i-1]) return false;
    }
    return true;
}

int main(){
#ifdef SSU
    freopen("input4.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
#endif
    srand(time(0));

    int T=in();
    vector<ll> all;
    all.pb(1);
    all.pb(9);
    all.pb(4);
    for(int i=1;i<100000000;++i){
        ll cur=toll(tostr(i));
        if(cur>200000000000000ll) break;
        if(ispal(tostr(cur))){
            string cc=tostr(i);
            cc+=string(cc.rbegin(), cc.rend());
           //cout<<cc<<' '<<cur<<endl;

            all.pb(cur);
        }
        for(int j=0;j<10;++j){
            cur=toll2(tostr(i),j);
            if(cur>200000000000000ll) break;
            if(ispal(tostr(cur))){
                string cc=tostr(i);
                cc.pb('0'+j);
                cc+=string(cc.rbegin()+1, cc.rend());
                //cout<<cc<<' '<<cur<<endl;

                all.pb(cur);
            }
        }
    }
    sort(all.begin(), all.end());
   // cout<<all.size()<<endl;
    /*for(int i=1;i<1000000;++i){
        if(ispal(tostr(i)) && ispal(tostr(i*(ll)i))) cout<<i<<' '<<(i*(ll)i)<<endl;
    }*/
     for(int t=1;t<=T;++t){
        ll a,b;
        cin>>a>>b;
        int res=upper_bound(all.begin(), all.end(), b) - lower_bound(all.begin(), all.end(),a);
        printf("Case #%d: %d\n", t, res);
    }



    return 0;
}
