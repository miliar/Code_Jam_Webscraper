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

int a[5][5],b[5][5],aa,bb,i,t,j,kk=1,k;

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    S(t);
    while(t--)
    {
        S(aa);
        for(i=1;i<=4;i++)for(j=1;j<=4;j++)S(a[i][j]);
        S(bb);
        for(i=1;i<=4;i++)for(j=1;j<=4;j++)S(b[i][j]);

        int cnt=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[aa][i]==b[bb][j]){ cnt++;k=a[aa][i]; break;}
            }
        }
        printf("Case #%d: ",kk++);
        if(cnt==1) printf("%d\n",k);
        else if(cnt>1) printf("Bad magician!\n");
        else if(cnt==0) printf("Volunteer cheated!\n");
    }

    return 0;
}












