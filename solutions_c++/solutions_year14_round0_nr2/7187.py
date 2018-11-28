#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
#include <limits.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define mset(mas,val) memset(mas,val,sizeof(mas))
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define getcx getchar//getchar_unlocked
inline void s( ll &n )
{
    n=0;

    ll ch=getcx();
    while( ch < '0' || ch > '9' )
    {
        ch=getcx();

    }

    while(  ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();

}
inline void s( int &n )
{
    n=0;

    int ch=getcx();
    while( ch < '0' || ch > '9' )
    {
        ch=getcx();

    }

    while(  ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();

}

int main()
{
   freopen("C:\\Users\\Nishant\\Desktop\\3.txt","r",stdin);
   freopen("C:\\Users\\Nishant\\Desktop\\1.txt","w",stdout);
    int t,u=0;
    s(t);
    while(t--)
    {
       u++;
        double c,f,x,rate=2,coins=0;
        cin>>c>>f>>x;
        double t=0;
        while(1)
        {
          double t1= (x-coins)/rate;
          double t2=-1;
          if(coins>=c)
          {
              t2=(x-(coins-c))/(rate+f);
          }
          else
          {
              t2 = c/rate+ x/(rate+f);
          }
          if(t2>=0)
          {
              if(t1<t2)
              {
                  t+=t1;
                  break;
              }
              else
              {
                  t+=c/rate;
                  rate+=f;
              }
          }
          else
          {
               t+=t1;
                  break;
          }
        }
        cout<<"CASE #"<<u<<": ";
        printf("%.7f\n",t);
    }
}
//cout<<"CASE #"<<u<<": "<<z<<endl;
