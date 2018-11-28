#define __LOCAL__
#define FILEINPUT 1

//#include<bits/stdc++.h>
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


#include<unordered_set>
#include<unordered_map>



#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;


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
#define ERR         (1e-7)
#define EQ(a,b)     (fabs((a)-(b))<ERR)
#define all(a)      (a).begin(),(a).end()
#define rall(a)      (a).rbegin(),(a).rend()
#define p2(a)       (1LL<<a)
#define EX(msk,a)   (msk&p2(a))
#define isInRange(v,l,h) (min(l,h)<=v && v<=max(l,h))




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


#define SIZE_N 100001000
#define SIZE_P 10000000

bool flag [SIZE_N];
int prime [SIZE_P];

void sieve ()
{
  int i, j, r, c = 1;

  for ( i = 3; i < SIZE_N; i += 2 )
        flag[i] = true ;
  flag [2] = true ;

  prime [c++] = 2 ;

  for ( i = 3; i <SIZE_N; i += 2 )
        if ( flag[i] )
    {
      prime[c++] = i ;

            if ( SIZE_N/i >= i )
            {
                r = i * 2 ;
                for ( j = i * i; j <SIZE_N; j += r )
                    flag[j] = false ;
            }
 
    }
}

void check(std::vector<int> &v,int n)
{
  for(int b=2;b<=10;b++)
  {
    ll val = 0,mul=1;
    ll cur = n;
      while(cur)
      {
        val += mul * (cur%2);
        cur/=2;
        mul*=b;
      }
      // debug(n,b,val);
      if(val < SIZE_N && flag[val] )
      {
        v.clear();
        return;
      }
      bool got = true;
      for(int p=1; prime[p] <= val / prime[p]; p ++)
        if(val%prime[p] == 0)          
      {
          got=false;
          v.pb(prime[p]);
          break;
      }
      if(got) {
        v.clear();
        return;
      }
  }
  return;
}

int main()
{
#ifdef FILEINPUT
    freopen("C-small-attempt0.in","r",stdin);
    // freopen("in.in","r",stdin);
   freopen("out.out","w",stdout);
#endif // FILEINPUT

   ios_base::sync_with_stdio(0);cin.tie(0);

   sieve();
   VI v;

   int tks,ks=1,n,J,cnt=0;
   scanf("%d",&tks);
   while(tks--){
    
      cin>>n>>J;
      cnt = 0;
      printf("Case #%d:\n",ks++);
      for(int i = p2(n-1)+1;i<p2(n);i++)
        if(i&1)
        {
          v.clear();
          check(v,i);
          if(SZ(v)==0)  continue;

          for(int j=n-1;j>-1;j--)
            printf("%d",( i & p2(j) ) > 0);
          for(int j=0;j<9;j++)
            cout<<" "<<v[j];
          cout<<endl;
          cnt++;
          if(--J == 0)  break;

        }
      // deb(cnt);
   }

   // while(scanf("")==){
   //     printf("\n");
   // }



    return 0;
}


//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;


