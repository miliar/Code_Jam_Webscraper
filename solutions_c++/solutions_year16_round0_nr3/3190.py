/// ///////////////////// ///
///                       ///
///      Tamanna_24       ///
///                       ///
///         JU            ///
///                       ///
/// ///////////////////// ///

#include<iostream>
#include<sstream>
#include<cstring>
#include<cstdio>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstdlib>
#include<cctype>

typedef long long ll;
typedef unsigned long long ull;

#define pi 2.0*acos(0.0)

template <class T> T _diff(T a,T b) {return (a<b?b-a:a-b);}
template <class T> T _abs(T a) {return(a<0?-a:a);}
template <class T> T _max(T a, T b) {return (a>b?a:b);}
template <class T> T _min(T a, T b) {return (a<b?a:b);}
template <class T> T max3(T a, T b, T c) {return (_max(a,b)>c ? _max(a,b) : c);}
template <class T> T min3(T a, T b, T c) {return (_min(a,b)<c ? _min(a,b) : c);}
template< class T>T GCD(T a,T b) {
    a=_abs(a);b=_abs(b);T tmp;while(a%b){ tmp=a%b; a=b; b=tmp; } return b;
}
template< class T>T LCM(T a,T b) {
    a=_abs(a);b=_abs(b);return (a/GCD(a,b))*b;
}
template<class T> T toRad(T deg) { return (deg*pi)/(180.0) ;}
template<class T> T toDeg(T rad) { return (rad*180.0)/(pi) ;}

#define pb(a) push_back(a)
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define S(a) scanf("%d",&a)
#define P(a) printf("%d",a)
#define PN() puts("")
#define PCASE() printf("Case #%d:\n",kk++)
#define eps 1e-9
#define inf 2000000000
#define mod 1000000007
#define MX  1000000
using namespace std;

ll jamCoin[50]={32769, 32773, 32775, 32777, 32781, 32787, 32793, 32795, 32799, 32805, 32811, 32815, 32817, 32821, 32823, 32827, 32829, 32835, 32841,
 32847, 32853, 32855, 32857, 32859, 32861, 32863, 32865, 32867, 32871, 32875, 32877, 32883, 32885, 32889, 32891, 32893, 32895, 32899, 32901, 32905,
 32913, 32919, 32921, 32923, 32925, 32931, 32935, 32937, 32947, 32949};

bool vis[100000002];
vector<ll>p;

void createPrime(){
    CLR(vis);
    p.clear();
    p.pb(2);
    for(ll i=3;i<=100000000;i+=2){
        if(vis[i]) continue;
        p.pb(i);
        for(ll j=i*3;j<=100000000; j+=i*2) vis[j]=1;
    }
}

ll getDivider(ll y){
    for(int i=0;i<p.size();i++){
        if(y%p[i]==0) return p[i];
    }
}

ll convertBase(ll val, ll base){
    ll m=1,s=0;
    while(val){
        s+=(m*(val%2));
        m*=base;
        val/=2;
    }
    return s;
}

void createLegi(){

    for(ll i=0;i<50;i++){
        cout<<convertBase(jamCoin[i],10)<<" ";
        for(ll j=2;j<=9;j++){
            ll y=convertBase(jamCoin[i],j);
            cout<<getDivider(y)<<" ";
        }
        cout<<getDivider(convertBase(jamCoin[i],10))<<endl;
    }
}

int main()
{
    createPrime();
    freopen("c.in","r",stdin);
    freopen("c1.txt","w",stdout);

    int t,kk=1,n,j;
    cin>>t;
    while(t--){
        cin>>n>>j;
        PCASE();
        createLegi();
    }

return 0;
}









