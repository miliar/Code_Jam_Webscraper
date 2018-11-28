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

struct data
{
    int x;
    char c;
};

vector<data>v[105];
string s;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int t,i,kk=1,j,k,n,res;

    S(t);
    data tmp;
    while(t--)
    {
        for(i=0;i<105;i++)v[i].clear();

        S(n);
        for(i=0;i<n;i++)
        {
            cin>>s;
            k=1;
            char c=s[0];
            for(j=1;j<s.size();j++)
            {
                if(s[j]==c)k++;
                else
                {
                    tmp.c=c;
                    tmp.x=k;
                    v[i].pb(tmp);

                    c=s[j];k=1;
                }
            }
            tmp.c=c;tmp.x=k;v[i].pb(tmp);
        }

        bool f=1;
        for(i=1;i<n;i++)
        {
            if(v[i].size()!=v[i-1].size())f=0;
        }
        if(f)
        {
            for(j=0;j<v[0].size();j++)
            {
                for(i=0;i<n;i++)
                {
                    if(v[i][j].c!=v[0][j].c) {f=0;break;}
                }
            }
        }
        if(!f)
        {
            printf("Case #%d: Fegla Won\n",kk++);
            continue;
        }
        int mx=0;
        for(j=0;j<v[0].size();j++)
        {
            int hi=0,low=1000;
            for(i=0;i<n;i++)
            {
                hi=max(hi,v[i][j].x);
                low=min(low,v[i][j].x);
            }
            int tm=0;res=1000;
            for(;low<=hi;low++)
            {
                tm=0;
                for(i=0;i<n;i++)
                {
                    if(low>v[i][j].x) tm+=(low-v[i][j].x);
                    else tm+=(v[i][j].x-low);
                }
                res=min(res,tm);
            }
            mx+=res;
        }
        printf("Case #%d: %d\n",kk++,mx);
    }

    return 0;
}












