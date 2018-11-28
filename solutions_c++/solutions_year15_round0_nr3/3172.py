/* Copyright (c) 2015 Martin Váňa */

/* http://www.cplusplus.com/reference/ */
/* C Library */
// #include <cassert>           // Diagnostics Library
#include <cctype>            // Character handling functions
// #include <cfenv>             // Floating-point environment
#include <cfloat>            // Characteristics of floating-point types
// #include <cinttypes>         // C integer types - C++11 feature
#include <climits>           // Sizes of integral types
#include <cmath>             // C numerics library
// #include <cstdint>           // Integer types
#include <cstdio>            // C library to perform Input/Output operations
#include <cstdlib>           // C Standard General Utilities Library
#include <cstring>           // C Strings

/* Containers */
#include <array>             // Array header
#include <bitset>            // Bitset header
#include <deque>             // Deque header
// #include <forward_list>      // Forward list - C++11 feature
#include <list>              // List header
#include <map>               // Map header
#include <queue>             // Queue header
#include <set>               // Set header
#include <stack>             // Stack
// #include <unordered_map>     // Unordered map header - C++11 feature
// #include <unordered_set>     // Unordered set header - C++11 feature
#include <vector>            // Vector header

/* Input/Output Stream Library */
// #include <fstream>           // File streams
#include <iostream>          // Standard Input / Output Streams Library
#include <sstream>           // String streams

/* Miscellaneous headers */
#include <algorithm>         // Standard Template Library: Algorithms
#include <complex>           // Complex numbers library
// #include <exception>         // Standard exceptions
// #include <functional>        // Function objects
// #include <initializer_list>  // Initializer list - C++11 feature
#include <iterator>          // Iterator definitions
// #include <limits>            // Numeric limits
// #include <numeric>           // Generalized numeric operations
// #include <random>            // Random - C++11 feature
// #include <ratio>             // Ratio header - C++11 feature
// #include <regex>             // Regular Expressions - C++11 feature
// #include <stdexcept>         // Exception classes
#include <string>            // Strings
// #include <tuple>             // Tuple library - C++11 feature
// #include <typeindex>         // Type index - C++11 feature
// #include <typeinfo>          // Type information
// #include <type_traits>       // Type traits - C++11 feature
// #include <utility>           // Utility components
// #include <valarray>          // Library for arrays of numeric values

using namespace std;

// Debug printing
#ifdef DEBUG
#define DBG(args...)                printf("DBG> ");printf(args);
#else
#define DBG(args...)                // Just strip off all debug tokens
#endif

// Printing
#define PR(args...)                 printf(args)

// Useful constants
#define STR_BUF                     256
#define INF                         INT_MAX
#define EPS                         1e-15
#define PI                          3.1415926535897932384626433832795

// Input macros
#define S(n)                        scanf("%d",&n)
#define SC(n)                       scanf("%c",&n)
#define SL(n)                       scanf("%lld",&n)
#define SF(n)                       scanf("%lf",&n)
#define SS(n)                       scanf("%s",n)

// For loops
#define F(i,L,U)                    for((i)=(L);(i)<(U);(i)++)
#define FE(i,L,U)                   for((i)=(L);(i)<=(U);(i)++)
#define RF(i,L,U)                   for((i)=(U);(i)>(L);(i)--)
#define RFE(i,L,U)                  for((i)=(U);(i)>=(L);(i)--)

// Checking bounds
#define IN(i,l,r)                   ((l)<(i)&&(i)<(r))
#define LINR(i,l,r)                 ((l)<=(i)&&(i)<=(r))
#define LIN(i,l,r)                  ((l)<=(i)&&(i)<(r))
#define INR(i,l,r)                  ((l)<(i)&&(i)<=(r))

// Bit operations
#define OR(a,b)                     ((a)|(b))
#define AND(a,b)                    ((a)&(b))
#define XOR(a,b)                    ((a)^(b))
#define BIT(x,i)                    ((x)&(1<<(i)))       //select the bit of position i of x
#define LBIT(x)                     ((x)&((x)^((x)-1)))  //get the lowest bit of x

// Some common useful functions
#define SIGN(x)                     ((x)>0)-((x)<0)
#define ABS(x)                      ((x)<0?(-(x)):(x))
#define MIN(a,b)                    (((a)<(b))?(a):(b))
#define MAX(a,b)                    (((a)>(b))?(a):(b))
#define REMAX(a,b)                  (a)=MAX((a),(b));      // set a to the maximum of a and b
#define REMIN(a,b)                  (a)=MIN((a),(b));
#define CB(n,b)                     (((n)>>(b))&1)
#define C2I(c)                      (c-'0')               // char to int
#define DROUND(num)                 (int)floor((num)+0.5) // Rounds num to int (int)num+(<.5 to 0, > .5 to 1)
#define IS_ODD(n)                   ((n)%2!=0)

// Variable definitions
#define DI(n)                       int n
#define DD(n)                       double n
#define DS(s,N)                     char s[N]
#define DIS(n)                      DI(n);S(n)

// Contest
#define TESTS                       DIS(_tc_no_);while(_tc_no_--)
#define CASES(cases)                S(cases);DI(_case_);FE(_case_,1,cases)
#define LINE(line)                  fgets(line,sizeof(line),stdin)
#define LINE_BY_LINE(line)          while(LINE(line))
#define DEF_SEP_LINE                DI(_fline_);_fline_=1;   // separate test cases with blank line
#define SEP_LINE                    (_fline_==1)?_fline_=0:PR("\n")

// Arrays
#define CLR(a,v)                    memset(a,v,sizeof(a))  // set elements of array to some value
#define PRAI(i,a,L,R)               F(i,L,R){PR("%d ",a[i]);}PR("\n")
#define PRAF(i,a,L,R)               F(i,L,R){PR("%lf ",a[i]);}PR("\n")
#define PRAS(i,a,L,R)               F(i,L,R){PR("%s ",a[i]);}PR("\n")

// Colections
#define ALL(c)                      (c).begin(), (c).end()
#define PB                          push_back

// Data types
#define LL                          long long
#define ULL                         unsigned long long
#define UI                          unsigned int
#define US                          unsigned short
#define II                          pair<int, int>
#define VII                         vector<II>
#define VI                          vector<int>


// Problem complex structures and algorithms

// Problem specific data

int l,x;
vector<LL> i_end;
vector<LL> k_start;
char word[100000];

int convert[5][5] = {
    {0, 0,  0,  0,  0},
    {0, 1,  2,  3,  4},
    {0, 2, -1,  4, -3},
    {0, 3, -4, -1,  2},
    {0, 4,  3, -2, -1}
};

int char2int(char a){
    switch(a){
        case 'i':
        return 2;

        case 'j':
        return 3;

        case 'k':
        return 4;
    }
    DBG("%c !!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",a);
    return 0;// should not reach
}

int calc(int a, int b){
    if (a*b >= 0){
        return convert[ABS(a)][ABS(b)];
    }else{
        return -convert[ABS(a)][ABS(b)];
    }
}

bool find_i()
{
    int i,j,result;
    result = 1;
    F(i,0,x){
        F(j,0,l)
        {
            result = calc(result, char2int(word[j]));
            if (result == char2int('i')){
                i_end.PB(i*l + j);
            }
        }
    }

    if (i_end.size() > 0){
        return true;
    }
    DBG("no i-s\n");
    return false;
}

bool find_k()
{
    int i,j,result;
    result = 1;
    RFE(i,0,x-1){
        RFE(j,0,l-1)
        {
            result = calc(char2int(word[j]), result);
            if (result == char2int('k')){
                k_start.PB(i*l + j);
            }
        }
    }

    if (k_start.size() > 0){
        return true;
    }
    DBG("no k-s\n");
    return false;
}

bool find_j()
{
    int i,ii,j,jj,result,start;
    F(i,0,(int)i_end.size())
    {
        F(j,0,(int)k_start.size())
        {
            if (i_end[i] >= k_start[j])
            {
                continue;
            }
            result = 1;
            start = (i_end[i] + 1) % l;

            F(ii,i_end[i] / l,x){
                F(jj,start,l)
                {
                    if (ii*l + jj == k_start[j]){
                        goto Fl;
                    }
                    // DBG("mult %c\n",word[jj]);
                    result = calc(result, char2int(word[jj]));
                }
                start = 0;
            }
            Fl:
            // DBG("end res=%d\n",result);
            if (result == char2int('j')){
                return true;
            }
        }
    }
    DBG("no j-s\n");
    return false;
}

bool check_word()
{
    int i,j,result;
    result = 1;
    F(i,0,x){
        F(j,0,l)
        {
            result = calc(result, char2int(word[j]));
        }
    }

    if (result == -1){
        return true;
    }
    return false;
}

int main( int argc, char *argv[] )
{
    int cases;
    bool match;

    CASES(cases)
    {
        S(l);
        S(x);
        match = false;
        i_end.clear();
        k_start.clear();
        SS(word);
        DBG("%s\n",word);
        if (((int)strlen(word)) * x >= 3 && check_word() && find_i() && find_k()){
            match = find_j();
        }

        if (match){
            PR("Case #%d: YES\n", _case_);
        }else{
            PR("Case #%d: NO\n", _case_);
        }
    }
    exit( EXIT_SUCCESS );
}
