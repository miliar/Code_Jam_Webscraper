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
#define PCASE() printf("Case %d: ",kk++)
#define eps 1e-9
#define inf 2000000000
#define mod 1000000007
#define MX  1000000
using namespace std;

int t,kk=1;
int p[1005],d,i,j,k,mn,nw,cnt;

int main()
{
    freopen("b.txt","r",stdin);
    freopen("b1.txt","w",stdout);
    S(t);
    while(t--){

        S(d);
        for(i=0;i<d;i++)S(p[i]);
        sort(p,p+d);

        mn=p[d-1];

        for(i=1;i<p[d-1];i++){
            nw=0;
            for(j=0;j<d;j++){
                if(p[j]<=i) continue;
                k=p[j]-i;
                cnt=(k/i)+ ((k%i)>0?1:0);
                nw+=cnt;
            }
            mn=min(mn, nw+i);
        }
        cout<<"Case #"<<kk++<<": "<<mn<<endl;
    }

    return 0;
}
