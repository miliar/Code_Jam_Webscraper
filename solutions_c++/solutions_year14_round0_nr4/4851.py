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

double tmp;
int a[1005],b[1005];
bool vis[1005];
int s,e,n,t,x,y,kk=1,i,j;

int main()
{
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
    S(t);
    while(t--)
    {
        S(n);
        for(i=1;i<=n;i++){scanf("%lf",&tmp);tmp*=10000.0; a[i]=((int)tmp); }
        for(i=1;i<=n;i++){scanf("%lf",&tmp);tmp*=10000.0; b[i]=((int)tmp); }

        sort(a+1,a+n+1);
        sort(b+1,b+n+1);

        x=0;y=0;
        CLR(vis);

        ///war.......

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(vis[j]==0 && b[j]>a[i]){vis[j]=1;break;}
            }
            if(j==n+1)
            {
                y++;
                for(j=1;j<=n;j++)
                {
                    if(vis[j]==0){vis[j]=1;break;}
                }
            }
        }

        /// D-war......

        s=1;e=n;
        for(i=1;i<=n;i++)
        {
            if(b[s]<a[i])
            {
                s++;x++;
            }
            else
            {
                e--;
            }
        }
        printf("Case #%d: %d %d\n",kk++,x,y);
    }

    return 0;
}












