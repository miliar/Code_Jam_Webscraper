#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <utility>
#include <functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <assert.h>






#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;


//#include<unordered_set>
//#include<unordered_map>

#define popcount(a) (__builtin_popcountll(a))
#define SZ(a)       ((int)a.size())
#define fs           first
#define sc           second
#define pb          push_back
#define ll          long long
#define ld          long double
#define MP          make_pair
#define SS          stringstream
#define VS          vector<string>
#define VI          vector<int>
#define CON(a,b)  ((a).find(b)!=(a).end())
#define mem(a,b)    memset(a,b,sizeof(a))
#define memc(a,b)   memcpy(a,b,sizeof(b))
#define accu(a,b,c) accumulate((a),(b),(c))
#define fii(a,b)    for(int i=a;i<b;i++)
#define fij(a,b)    for(int j=a;j<b;j++)
#define fik(a,b)    for(int k=a;k<b;k++)
#define fil(a,b)    for(int l=a;l<b;l++)
#define ri(i,a)     for(int i=0;i<a;i++)
#define rii(a)      for(int i=0;i<a;i++)
#define rij(a)      for(int j=0;j<a;j++)
#define rik(a)      for(int k=0;k<a;k++)
#define fore(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define ERR         (1e-10)
#define EQ(a,b)     (fabs((a)-(b))<ERR)
#define all(a)      (a).begin(),(a).end()
#define rall(a)      (a).rbegin(),(a).rend()
#define p2(a)       (1LL<<a)
#define EX(msk,a)   (msk&p2(a))
#define isInRange(v,l,h) (min(l,h)<=v && v<=max(l,h))


#define __LOCAL__

#ifdef __LOCAL__
	#define deb(a)      cerr<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
	// #define deb(a)      cout<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
#define debug(a...)          {cout<<" #--> ";dbg,a; cout<<endl;}

struct debugger
{
    ///Collected from rudradevbasak
    template<typename T> debugger& operator , (const T v)
    {
        cout<<v<<" ";
        return *this;
    }
} dbg;
#else

#define deb(a) ;
#define debug(a...)  ;

#endif



const double pi=acos(-1.0);
const double eps=1e-7;

template<class TT>TT sqr(TT a){return a*a;}
template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
typedef pair<int,int> pii;

const int S  =18;
bool flg[S];
double p[S];
vector<double>v;
int h;
double mm[S][S/2][S/2];

double go(int pos,int x,int y)
{

    if(x<0 || y<0)  return 0;
    if(x+y==0)  return 1;
    if(pos < 0) return 0;

    double &re = mm[pos][x][y];
    if(re>-1)   return re;
    re = 0;
//    re = max( go(pos-1,x,y), p[pos]*go(pos-1,x-1,y) + (1-p[pos])*go(pos-1,x,y-1) );

    re = v[pos] * go(pos-1,x-1,y) + (1 - v[pos]) * go(pos-1,x,y-1) ;
//    debug(re,pos,x,y);

    return re;
}

void Clear()
{
    int i,j,k;
    rii(S)
        rij(S/2)
            rik(S/2)
                mm[i][j][k] = -5;
}

int main()
{
//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;


//    freopen("in1.in","r",stdin);
    freopen("B-small-attempt2.in","r",stdin);
//    freopen("B-small-attempt1.in","r",stdin);
    freopen("out1.in","w",stdout);

    int i,j,n,k;

    int tks,ks=1;

    cin>>tks;
    while(tks--)
    {
//        deb("Maksud");
        Clear();
        mem(flg,true);

        cin>>n>>k;
//        deb("Maksud");
        h = k/2;
        rii(n)
            cin>>p[i];

        int m=h;
        double ans;
        double Max = 0;
        int a,b;
        int MSK;

        for(int msk = 3;msk<p2(n);msk++)
            if(popcount(msk)==k)
            {
                v.clear();
                rii(n)
                    if(EX(msk,i))
                    {
                        v.pb(p[i]);
                    }
                Clear();
                ans = go(k-1,h,h);
                Max = max(Max,ans);
                if(EQ(Max,ans))
                {
                    MSK = msk;
                }
            }

//        rii(n)
//            if(EX(MSK,i))
//                deb(p[i]);
        printf("Case #%d: %.10lf\n",ks++,Max);
    }

    return 0;
}




