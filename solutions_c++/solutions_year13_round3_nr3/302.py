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
#define rep(i,n) for(int i=0;i<n;++i)
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


bool iscon(char c){
    if(c=='a' || c=='o' || c=='e' || c=='u' || c=='i') return 0;
    return 1;
}
vector<vector<int> > ans;
int res=0;
void dfs(int x, int y, int d, int an){
    if(an>100) return;
    if(x>=0 && y>=0 && x<=100 && y<=100){
        if(ans[x][y]!=-1) return;
        ans[x][y]=an;
        res++;
        cout<<res<<endl;
    }
    an++;
    dfs(x-d, y, d+1, an);
    dfs(x+d, y, d+1, an);
    dfs(x, y-d, d+1, an);
    dfs(x, y+d, d+1, an);
}
struct trib{
    ll firsd;
    ll n;
    ll l, r;
    ll s;
    ll deld;
    ll deldist;
    ll dels;
};
struct att{
    ll curd;
    ll l, r;
    ll s;
};
bool comp(const att a, const att b){
    return a.curd<b.curd;
}

int main(){
#ifdef SSU
    freopen("cc1.in", "r", stdin);
      freopen("output.txt", "w", stdout);
#endif


    int T=in();
    for(int t=0;t<T;++t){
        int n=in();
        vector<trib> v;
        ll ans=0;
        for(int i=0;i<n;++i){
            trib cur;
            cur.firsd=in();
            cur.n=in();
            cur.l=in();
            cur.r=in();
            cur.s=in();
            cur.deld=in();
            cur.deldist=in();
            cur.dels=in();
            v.pb(cur);
        }
        vector<att> a;
        ll mid=50000;
        for(int i=0;i<v.size();++i){
            trib cur=v[i];
            ll curd=cur.firsd;
            ll str=cur.s;
            ll curl=cur.l;
            ll curr=cur.r;
            for(int j=1;j<=cur.n;++j){
                att at;
                at.curd=curd;
                at.s=str;
                at.l=curl*4+mid;
                at.r=curr*4+mid;
                a.pb(at);

                curd+=cur.deld;
                str+=cur.dels;
                curl+=cur.deldist;
                curr+=cur.deldist;
            }
        }
        sort(a.begin(), a.end(), comp);
        int lastd=0;
        vector<ll> wall(100000, 0);
        vector<ll> w=wall;
        for(int i=0;i<a.size();++i){
            att cur=a[i];
            if(cur.curd>lastd) wall=w;
            bool ta=0;
            for(int j=cur.l;j<=cur.r;++j){
                if(wall[j]<cur.s){
                    ta=1;
                    w[j]=max(cur.s, w[j]);
                }
            }
            if(ta) ans++;
            lastd=cur.curd;
        }
        printf("Case #%d: %lld\n", t+1, ans);




    }


  /* int T=in();
    for(int t=0;t<T;++t){
        printf("Case #%d: ",t+1);
        int x=in(), y=in();
        int cx=y, cy=x;
        while(cx!=0){
            if((cx>0)){
                printf("SN");
            }else printf("NS");
            if(cx<0) cx++;
            else cx--;
        }
        while(cy){
            if((cy>0)){
                printf("WE");
            }else printf("EW");
            if(cy<0) cy++;
            else cy--;
        }
        fflush(stdout);
        puts("");
    }
    fflush(stdout);*/

    /* int T=in();
    for(int t=0;t<T;++t){
        string s;
        cin>>s;
        vector<int> v(s.size(),0);
        int n=in();
        for(int i=0;i<s.size();++i){
            if(iscon(s[i])) v[i]=1;
        }
        vector<int> d(s.size(),0);
        d[0]=v[0];
        for(int i=1;i<s.size();++i){
            if(v[i]){
                d[i]=d[i-1]+1;
            }
        }
        for(int i=0;i<d.size();++i){
            if(d[i]<n) d[i]=0;
            else{
                d[i]=0;
                d[i-n+1]=1;
            }
        }
        vector<int> a;
        for(int i=0;i<d.size();++i){
            if(d[i]) a.pb(i);
        }
        ll ans=0;
        for(int i=0;i<s.size();++i){
            vector<int>::iterator to=lower_bound(a.begin(), a.end(), i);
            if(to!=a.end())
            ans+=s.size()-(*to+n-1);
        }
        printf("Case #%d: %lld\n", t+1, ans);


    }*/







    return 0;
}
