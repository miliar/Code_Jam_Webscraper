/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define ins insert
#define mp make_pair
#define sz(x) ((int)x.size())
#define clr clear()
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define sqr(x) ((x)*(x))
#define mem(x,val) memset((x),(val),sizeof(x));
#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);
#define chk(a,k) ((bool)(a&(1<<(k))))
#define off(a,k) (a&(~(1<<(k))))
#define on(a,k) (a|(1<<(k)))

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;
typedef pair<i64,i64> pii;
typedef vector<pii> vpii;

#define mx 0
#define mod 1000002013LL

i64 powmod( long long b, i64 p, i64 m )
{
    long long r = 1;
    for( i64 i = ( 1 << 30 ); i; i >>= 1 )
    {
        r *= r; r %= m;
        if( p & i ) { r *= b; r %= m; }
    }
    return r;
}

i64 inv=powmod(2,mod-2,mod);

struct data{
    int xx,yy,c;
    data(int _u,int _v,int _c){
        xx=_u, yy=_v, c=_c;
    }
    bool inside(data b){
        return (
                (b.xx<=xx && yy<=b.yy)
                );
    }
    i64 cost(i64 n){
        i64 s=yy-xx;
        //cout<<"s="<<s<<endl;
        s*=n;
        s%=mod;
        rep(ii,yy-xx){
            s-=ii;
            if(s<0) s+=mod;
        }
        return s;
    }
};

int main(){
    //cout<<(2*powmod(2,mod-2,mod))%mod<<endl;
    read("Ain.txt");
    rite("Aout.txt");
	double cl = clock();
    cl = clock() - cl;
    int test,kas=0;
    cin>>test;
    while(test--){
        printf("Case #%d: ",++kas);
        vector< data > vec;
        i64 n,m;
        cin>>n>>m;
        i64 tot=0;
        rep(i,m){
            int a,b,c;
            cin>>a>>b>>c;
            //cout<<"-0-"<<endl;
            //cout<<data(a,b,c).cost(n)<<endl;
            //cout<<"-0-"<<endl;
            tot+=(data(a,b,c).cost(n)*i64(c))%mod;
            tot%=mod;
            while(c--)
            vec.pb( data(a,b,c) );
        }
        //cout<<tot<<endl;
        while(true){
            int f=0;
            rep(i,sz(vec)){
                rep(j,sz(vec)){
                    if(i==j) continue;
                    if(vec[i].inside(vec[j])) continue;
                    if(vec[j].inside(vec[i])) continue;
                    //if(vec[i].yy<vec[j].xx && vec[j].yy<vec[i].xx) continue;

                    if(vec[i].xx<= vec[j].xx && vec[i].yy>=vec[j].xx){
                        f=1;
                        int temp=vec[i].yy;
                        vec[i].yy=vec[j].yy;
                        vec[j].yy=temp;
                    }
                    else if(vec[j].xx<= vec[i].xx && vec[j].yy>=vec[i].xx){
                        f=1;
                        //cout<<vec[i].xx<<","<<vec[i].yy<<endl;
                        //cout<<vec[j].xx<<","<<vec[j].yy<<endl;
                        int temp=vec[j].yy;
                        vec[j].yy=vec[i].yy;
                        vec[i].yy=temp;
                    }
                }
            }
            if(!f) break;
            //cout<<"here"<<endl;
        }
        i64 now=0;
        rep(i,sz(vec)){
            now+=vec[i].cost(n);
            now%=mod;
        }
        cout<<(tot-now+mod)%mod<<endl;
    }
    fprintf(stderr, "Total Execution Time = %lf seconds", cl / CLOCKS_PER_SEC);
    return 0;
}
