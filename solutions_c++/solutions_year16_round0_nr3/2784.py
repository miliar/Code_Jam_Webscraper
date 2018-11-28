// ==========================================================================
//
//                   Bismillah ir-Rahman ir-Rahim
//
// ==========================================================================

/*************************************************************************
  ████      ▀███▀    ▄▄▄▀▀▀▀▄▄▄   █▀▄▀▄▀▄▀▄▀▄█  ▀███▀   ████       ████
  ███ █      ███     ███    ███              █   ███    ███ █     █ ███
  ███  █     ███     ███    ███            █     ███    ███  █   █  ███
  ███   █    ███     ███    ███          █       ███    ███   █▄█   ███
  ███    █   ███     ███▀▀▀▀███        █         ███    ███         ███
  ███     █  ███     ███    ███      █           ███    ███         ███
  ███      █ ███     ███    ███    █             ███    ███         ███
 ▄███▄      ████     ███    ███   █▄▀▄▀▄▀▄▀▄▀█  ▄███▄  ▄███▄       ▄███▄
**************************************************************************/

//#include <bits/stdc++.h>

// header file

#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <fstream>
#include <numeric>
#include <cstring>

using namespace std ;

//define function

#define forln(i,a,n) for(int i=a ; i<n ; i++)
#define foren(i,a,n) for(int i=a ; i<=n ; i++)
#define forg0(i,a,n) for(int i=a ; i>n ; i--)
#define fore0(i,a,n) for(int i=a ; i>=n ; i--)
#define pb push_back
#define pp pop_back
#define clr(a,b) memset(a,b,sizeof(a))
#define sf1(a) scanf("%d",&a)
#define sf2(a,b) scanf("%d %d",&a,&b)
#define sf1ll(a) scanf("%lld",&a)
#define sf2ll(a,b) scanf("%lld %lld",&a,&b)
#define pii acos(-1.0)
#define jora_int pair<int,int>
#define jora_ll pair<long long,long long>
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define Max 1000000000000000000+9
#define sz 100000000+7
#define Mod 1000000007
#define EPS 1e-10
#define ll long long
#define ull unsigned long long
#define fs first
#define sc second
#define wait system("pause")
#define sf scanf
#define pf printf
#define mp make_pair
#define ps pf("PASS\n")
#define Read freopen("input.txt","r",stdin)
#define Write freopen("output.txt","w",stdout)

//debug

template<class T1> void deb(T1 e1)
{
    cout<<e1<<endl;
}
template<class T1,class T2> void deb(T1 e1,T2 e2)
{
    cout<<e1<<" "<<e2<<endl;
}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3)
{
    cout<<e1<<" "<<e2<<" "<<e3<<endl;
}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;
}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;
}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;
}

// moves

//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//int dx[]= {0,0,1,-1};/*4 side move*/
//int dy[]= {-1,1,0,0};/*4 side move*/
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*night move*/


//close

/// --------------------------------------------- EOP --------------------------------------------- ///

vector<ll>vec , primes , tans ;
bool arr[sz] ;

void seave()
{
    arr[1] = 1 ;

    primes.pb(2);

    for(int i=4 ; i<sz ; i+=2)
        arr[i] = 1 ;

    for(int i=3 ; i < sz ; i++)
    {
        if(!arr[i])
        {
            primes.pb(i);

            if(1LL*i*i >= sz)
                continue;

            for(int j=i*i ; j<sz ; j+=i)
                arr[j] = 1 ;
        }
    }
//    deb(primes.back());
}

ll POW(ll base,ll p)
{
    ll ans = 1 ;

    while(p>0)
    {
        ans *= base ;
        p--;
    }
    return ans ;
}

void convert(int a)
{
    vec.clear();

    while(a)
    {
        vec.pb(a%2);
        a/=2 ;
    }
}

ll is_prime(ll a)
{
    ll ans , tp = a ;

    for(int i=0 ; i<primes.size() and primes[i]*primes[i] <=a ; i++)
    {
        if(a%primes[i] == 0)
            return primes[i] ;
    }

    return -1 ;
}

bool isok()
{
    ll ans  , tp ;
//for(int i=0 ; i<vec.size() ; i++)deb(vec[i]);
    for(int i=3 ; i<=10 ; i++)
    {
        ans = 0 ;

        for(int j=0 ; j<vec.size() ; j++)
        {
            if(vec[j] == 0)
                continue;

            ans += POW(i,j);
        }

        tp = is_prime(ans);

        if(tp == -1)
            return 0 ;

        tans.pb(tp);
    }

    return 1 ;
}

int main()
{
    Read;
    Write;
    seave();

    int tcase , ta , tb ;

    sf1(tcase);

    foren(cas,1,tcase)
    {
        sf2(ta,tb);
        ta-- ;

        ll a = (1<<ta) + 1 , cont = 0 , tp ;

        pf("Case #1:\n");

        for(ll i=a ; ; i+=2)
        {
            convert(i);

            tp = is_prime(i);

            if(tp == -1)
                continue;

            tans.clear();
            tans.pb(tp);

            if(isok())
            {
                for(int j=vec.size()-1 ; j>=0 ; j--)
                    pf("%lld",vec[j]);

                for(int j=0 ; j<tans.size() ; j++)
                    pf(" %lld",tans[j]);

                pf("\n");

                cont++;

                if(cont == tb)
                    break;
            }
        }
    }

    return 0 ;
}
