/********************************************************************************\
   |--\        ---       /\        |-----------| -----       /-------|           |
   |   \        |       /  \       |               |        /                    |
   |    \       |      /    \      |               |       |                     |
   |     \      |     /      \     |               |        \---\                |
   |      \     |    / ------ \    |-------|       |             \---\           |
   |       \    |   /          \   |               |                  |          |
   |        \   |  /            \  |               |                  /          |
  ---        \------            ------           -----     |---------/           |
                                                                                 |
                          _                                                      |
  **copyrighted by nfssdq(R) :) (:                                               |
                          ^                                                      |
    codeforces = nfssdq                                                          |
    topcoder = nafis007                                                          |
    uva = nfssdq                                                                 |
    spoj = nfssdq                                                                |
    usaco = nfssdq1                                                              |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                           |
    IIT,Jahangirnagar University(41)                                             |
    Sorry for badly written code.  :(                                            |
                                                                                 |
*********************************************************************************/
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <locale>
#include <string>
#include <vector>
#include <cassert>
#include <climits>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <iterator>
#include <typeinfo>
#include <valarray>
#include <algorithm>
#include <functional>
using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000002013ll
#define PI         2.0*acos(0.0)
#define linf       (1ll<<56)-1
#define FOR(I,A,B) for( I = (A); I < (B); ++I )
#define REP(I,N)   FOR( I, 0, N)
#define ALL(A)     ( (A).begin(), (A).end() )
#define set0(ar)   memset( ar, 0, sizeof ar )
#define vsort(v)   sort( ALL(v) )
#define SET(ar,v)  memset( ar, v, sizeof ar )
#define setinf(a)  SET(a,126)


template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0)return 1;
    if(e%2==0){LL t=bigmod(p,e/2,M);return (LL)((t*t)%M);}
    return ((LL)bigmod(p,e-1,M)*(LL)p)%M;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

LL ar[101][101];
LL in[101],out[101];
main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    LL a,b,c,d,e,f,g,h,i,j,k,l,x,y,z;
    cin>>a;
    for(z=1;z<=a;z++)
    {
        cin>>b>>c;
        d=0;
        set0(ar);set0(in);set0(out);
        for(x=0;x<c;x++)
        {
            cin>>e>>f>>g;
            h=b;
            for(y=e;y<=f;y++)
            {
                d=(d+h*g)%mod;
                h--;
            }
            in[e]+=g;
            out[f]+=g;
        }
        e=0;
        f=0;
        for(x=1;x<=b;x++)
        {
            f+=in[x];
            ar[x][b]+=in[x];
            g=out[x];
            for(y=b;y>=1;y--)
            {
                if(g==0)break;
                if(ar[x][y]>=g)
                {
                    e=(e+y*g)%mod;
                    ar[x][y]-=g;
                    g=0;
                }
                else
                {
                    e=(e+y*ar[x][y])%mod;
                    g-=ar[x][y];
                    ar[x][y]=0;
                }
            }
            f-=out[x];
            for(y=b;y>=1;y--)
            {
                e=(e+ar[x][y]*y);
                ar[x+1][y-1]=ar[x][y];
            }
        }
        d=(d-e);
        if(d<0)d+=mod;
        cout<<"Case #"<<z<<": "<< d   <<endl;
        cerr<<"Case #"<<z<<": "<< d  <<endl;
    }
}


