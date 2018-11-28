//#include<bits/stdc++.h>
#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <assert.h>
#include<unordered_set>
#include<unordered_map>



#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;

#define deb(a)      cerr<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
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
#define VD          vector<double>
#define CON(a,b)  ((a).find(b)!=(a).end())
#define mem(a,b)    memset(a,b,sizeof(a))
#define memc(a,b)   memcpy(a,b,sizeof(b))
#define accu(a,b,c) accumulate((a),(b),(c))
#define fi(i,a,b)   for(i=a;i<b;i++)
#define fii(a,b)    for(i=a;i<b;i++)
#define fij(a,b)    for(j=a;j<b;j++)
#define fik(a,b)    for(k=a;k<b;k++)
#define fil(a,b)    for(l=a;l<b;l++)
#define ri(i,a)     for(i=0;i<a;i++)
#define rii(a)      for(i=0;i<a;i++)
#define rij(a)      for(j=0;j<a;j++)
#define rik(a)      for(k=0;k<a;k++)
#define ril(a)      for(l=0;l<a;l++)
#define fore(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define ERR         (1e-7)
#define EQ(a,b)     (fabs((a)-(b))<ERR)
#define all(a)      (a).begin(),(a).end()
#define rall(a)      (a).rbegin(),(a).rend()
#define p2(a)       (1LL<<a)
#define EX(msk,a)   (msk&p2(a))




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


const double pi=acos(-1.0);
const double eps=1e-7;

template<class TT>TT sqr(TT a){return a*a;}
template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
typedef pair<int,int> pii;

long double ans()
{
    double mx,mn,V,X,spmx,spmn,r,c;
    int n,i;
    vector<double> R,C;
    scanf("%d",&n);
    cin>>V>>X;

    cin>>r>>c;
    R.pb(r);
    C.pb(c);


    mx=mn=c;
    spmx=spmn=r;
    fii(1,n)
    {
        cin>>r>>c;
        R.pb(r);
        C.pb(c);
        mx = max(mx,c);
        mn = min(mn,c);

        spmx = max(spmx,r);
        spmn = min(spmn,r);

    }

    if(mn>X+eps)    return -11;
    if(mx+eps<X)    return -11;

    if(n==1)    return V/spmx;

    if(EQ(C[0],C[1]))
        return V/(R[0]+R[1]);

    long double low=0,hi=V,mid,dg;

    if(C[0]>C[1])
    {
        swap(C[0],C[1]);
        swap(R[0],R[1]);
    }
//    deb(1);

    rii(2000)
    {
        mid=(low+hi)/2;
        dg = (mid*C[0]+(V-mid)*C[1])/V;
        if(dg>X) low=mid;
        else hi=mid;
    }

    return max(mid/R[0],(V-mid)/R[1]);
}

int main()
{
//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;


//    freopen("in.in","r",stdin);
    freopen("B-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-large.in","r",stdin);
    freopen("out.in","w",stdout);




    int i,j,k,tks=1,ks=1,n;

    cin>>tks;



    while(tks--)
    {
        double a=ans();

        if(a<-1)   printf("Case #%d: IMPOSSIBLE\n",ks++);
        else printf("Case #%d: %.10lf\n",ks++,a);
    }


    return 0;
}




