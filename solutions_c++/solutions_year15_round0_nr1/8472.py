// profile : sunnyO4
// * Basic Template *
// fundamentals headers
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <iomanip>
#include <cassert>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <ctime>
// Include all header files
// #include <bits/stdc++.h>

using namespace std;

#define DEBUG

#ifdef DEBUG

    #define debug(args...)     (Debugger()) , args

    class Debugger
    {
        public:
        Debugger(const std::string& _separator = ", ") :
        first(true), separator(_separator){}

        template<typename ObjectType>
        Debugger& operator , (const ObjectType& v)
        {
            if(!first)
                std:cerr << separator;
            std::cerr << v;
            first = false;
            return *this;
        }
        ~Debugger() {  std:cerr << endl;}

        private:
        bool first;
        std::string separator;
    };
#else
    #define debug(args...)                  // Just strip off all debug tokens
#endif

// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define checkbit(n,b)                ( (n >> b) & 1)

// Useful container manipulation / traversal macros
#define FOR(i,a,b,incr)                  for(int i=a;i<b;i+= incr)
#define RFOR(i,a,b,decr)                 for(int i=a;i>=b;i-= decr)

// Input macros
#define s(n)                        scanf("%d",&n)
#define su(n)                       scanf("%u",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define sc(n)                       scanf("%c",&n)
#define ss(n)                       scanf("%s",&n)

// Useful constants
#define INF         (int)1E9
#define EPS         1.0E-8
#define eql(a,b)    fabs(a-b) < EPS
#define mp          make_pair
#define pb          push_back
#define ppb         pop_back
#define sd          second
#define fs          first


typedef long long int ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair<int,int> pint;
typedef vector<string> vs;
typedef vector<int> vi;


/*--------------- Main Code here  -------------------------------*/

#define SIZE        1000

int shy_arr[1010];

int main()
{

    //freopen("read.in","r",stdin); freopen("out.in","w",stdout);

    int tc;
    s(tc);
    FOR(ind,1,tc+1,1){

        printf("Case #%d: ",ind);

        int smax; s(smax);
        string s;
        cin>>s;

        int len = s.length();

        FOR(i,0,len,1){
            shy_arr[i] = s[i] - '0';
        }

        int cnt = 0, add = 0;
        FOR(i,0,len, 1){
            cnt += shy_arr[i];
            if(i+1 > len -1)
                break;
            if(shy_arr[i+1] == 0){
                //debug(ind, cnt, i+1, shy_arr[i+1], add);
                continue;
            }
            else if(cnt+add < i+1){
                add += (i+1) - (cnt+add);
            }
            //debug(ind, cnt, i+1, shy_arr[i+1], add);
        }
        printf("%d\n", add);
    }

    return 0;
}
/*
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
*/
