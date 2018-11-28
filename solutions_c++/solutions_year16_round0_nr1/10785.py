
/*
"I'll Be There For You (Theme From Friends)"

So no one told you life was gonna be this way
Your job's a joke, you're broke, your love life's D.O.A.
It's like you're always stuck in second gear
When it hasn't been your day, your week, your month, or even your year, but

I'll be there for you
(When the rain starts to pour)
I'll be there for you
(Like I've been there before)
I'll be there for you
('Cause you're there for me too)

You're still in bed at ten and work began at eight
You've burned your breakfast, so far things are going great
Your mother warned you there'd be days like these
But she didn't tell you when the world has brought you down to your knees that

I'll be there for you
(When the rain starts to pour)
I'll be there for you
(Like I've been there before)
I'll be there for you
('Cause you're there for me too)

No one could ever know me
No one could ever see me
Seems you're the only one who knows what it's like to be me
Someone to face the day with, make it through all the rest with
Someone I'll always laugh with
Even at my worst, I'm best with you, yeah!

It's like you're always stuck in second gear
When it hasn't been your day, your week, your month, or even your year

I'll be there for you
(When the rain starts to pour)
I'll be there for you
(Like I've been there before)
I'll be there for you
('Cause you're there for me too)

I'll be there for you
(When the rain starts to pour)
I'll be there for you
(Like I've been there before)
I'll be there for you
('Cause you're there for me too)
*/

#ifndef _GLIBCXX_NO_ASSERT
#include <cassert>
#endif
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdalign>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
#endif

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif

#define sd(n)   scanf("%lld",&n)
#define pf(n)   printf("%lld\n",n)
#define pfs(n)  printf("%lld ",n)
#define nln     printf("\n")
#define all(v)  v.begin(),v.end()
#define pb      push_back
#define mp      make_pair
#define mt      make_tuple
#define eb      emplace_back
#define xx      first
#define yy      second
#define vll     vector<ll>
#define vpll    vector<pair<ll,ll>>
#define vppll   vector<pair<ll,pair<ll,ll>>>
#define vpllb   vector<pair<ll,bool>>
#define vpsll   vector<pair<string,ll>>
#define vplls   vector<pair<ll,string>>

using namespace std;

typedef long long   ll;
typedef long double ld;

const ll INF=LLONG_MAX;
const ll NINF=LLONG_MIN;
const ll MAX=2e6+5;
const ll MOD=1e9+7;

ll a[MAX];

int main()
{
    ll t,n,x,i,c;
    sd(t);
    while(t--)
    {
        sd(n);
        x=0;
        for(i=0;i<n;i++)
        {
            sd(a[i]);
            x=x^a[i];
        }
        if(x==0)
        {
            cout<<"First\n";
        }
        else
        {
            c=0;
            for(i=0;i<n;i++)
            {
                if(x^a[i]!=0)
                {
                    c=1;
                    break;
                }
            }
            if(c==0)
            {
                cout<<"Second\n";
            }
            else
            {
                if(n%2==0)
                {
                    cout<<"First\n";
                }
                else
                {
                    cout<<"Second\n";
                }
            }
        }
    }
}
