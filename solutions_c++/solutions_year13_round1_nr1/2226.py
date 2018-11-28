#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template <class T> T gcd(T a, T b) { return b==0 ? a : gcd(b,a%b) ; }
template <class T> T maxm(T a, T b) { return a > b ? a : b ; }
template <class T> T minm(T a, T b) { return a < b ? a : b ; }
template <class T> T abs(T a) { return a > 0 ? a : (-1)*a ; }
template <class T> T sq(T a) { return a * a ; }

#define clr(a) memset(a,0,sizeof(a))
#define set(a) memset(a,-1,sizeof(a))
#define R(a) freopen(a,"r",stdin)
#define W(t) while(t--)
#define forr(x, b, e)    for (int x = (b); x <= (e); x++)
#define S(n) scanf("%lld",&n)
#define pi 22/7

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);

    long long test,r,c,t;
    S(test);
    for(long long x=1;x<=test;x++)
    {
        c=0;
        S(r);
        scanf("%lld",&t);
        while(t>=0)
        {
            //cout<<((r+1)*(r+1))-(r*r)<<endl;
            t-=(((r+1)*(r+1))-(r*r));
            if(t>=0)
            {
                c++;
                r+=2;
            }
            else
                break;
        }
        printf("Case #%lld: %lld\n",x,c);
    }

    return 0;
}
