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
#include <unordered_set>     // Unordered set header - C++11 feature
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
// CP3 Bit operations
#define IS_ON(S, j)                 (S & (1 << j))
#define SET_BIT(S, j)               (S |= (1 << j))
#define CLEAR_BIT(S, j)             (S &= ~(1 << j))
#define TOOGLE_BIT(S, j)            (S ^= (1 << j))
#define LOW_BIT(S)                  (S & (-S))
#define SET_ALL(S, n)               (S = (1 << n) - 1)
// CP3 Bit operations
#define MODULO(S, N)                ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define IS_POWER_OF_TWO(S)          (!(S & (S - 1)))
#define NEAREST_POWER_OF_TWO(S)     ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define TURN_OFF_LAST_BIT(S)        ((S) & (S - 1))
#define TURN_ON_LAST_ZERO(S)        ((S) | (S + 1))
#define TURN_OFF_LAST_CONSECUTIVE_BITS(S)    ((S) & (S + 1))
#define TURN_ON_LAST_CONSECUTIVE_ZEROES(S)   ((S) | (S - 1))

// Some common useful functions
#define SIGN(x)                     ((x)>0)-((x)<0)
#define ABS(x)                      ((x)<0?(-(x)):(x))
#define MIN(a,b)                    (((a)<(b))?(a):(b))
#define MAX(a,b)                    (((a)>(b))?(a):(b))
#define REMAX(a,b)                  (a)=MAX((a),(b))      // set a to the maximum of a and b
#define REMIN(a,b)                  (a)=MIN((a),(b));
#define CB(n,b)                     (((n)>>(b))&1)
#define C2I(c)                      (c-'0')               // char to int
#define DIGITS(i)                   (int)((log(i)/log(10))+1)
#define DIGITSLL(i)                 (LL)((log(i)/log(10))+1)
#define DROUND(num)                 (int)floor((num)+0.5) // Rounds num to int (int)num+(<.5 to 0, > .5 to 1)
#define IS_ODD(n)                   ((n)%2!=0)

// Variable definitions
#define DI(n)                       int n
#define DD(n)                       double n
#define DS(s,N)                     char s[N]
#define DIS(n)                      DI(n);S(n)

// Contest
#define TESTS                       DIS(_tc_no_);while(_tc_no_--)
#define CASES                       int _c_no_,_case_;S(_c_no_);FE(_case_,1,_c_no_)
#define LINE(line)                  fgets(line,sizeof(line),stdin)
#define LINE_BY_LINE(line)          while(LINE(line))
#define DEF_SEP_LINE                DI(_fline_);_fline_=1;   // separate test cases with blank line
#define SEP_LINE                    (_fline_==1)?_fline_=0:PR("\n")

// Arrays
#define CLR(a,v)                    memset(a,v,sizeof(a))  // set elements of array to some value
#define PRAI(i,a,L,R)               F(i,L,R){PR("%d ",a[i]);}PR("\n")
#define PRAF(i,a,L,R)               F(i,L,R){PR("%lf ",a[i]);}PR("\n")
#define PRAS(i,a,L,R)               F(i,L,R){PR("%s ",a[i]);}PR("\n")

// Data types
typedef long long          LL;
typedef unsigned long long ULL;
typedef unsigned int       UI;
typedef unsigned short     US;
typedef pair<int, int>     II;
typedef vector<II>         VII;
typedef vector<int>        VI;


// Problem complex structures and algorithms

// Problem specific data


int main( int argc, char *argv[] )
{
    LL N,count,cur,s_cur,s_cur2,i,ma,di,last_i;
    char word[1000];
    pair<LL,LL> last = make_pair(0,0);// cur, s_cur

    CASES
    {
        SL(N);
        count = 0;
        cur = 0;

        if (N <= 20){
            count = N;
        }else{
            count = 12;
            cur = 12;
            while (true){
                sprintf(word, "%d\0",cur);
                reverse(word, word + strlen(word));
                s_cur = atol(word);
                if (s_cur > cur + 1 && s_cur <= N){
                    di = DIGITSLL(cur);
                    sprintf(word, "%d\0",cur);
                    F(i,(LL)(strlen(word) - strlen(word)/2), (LL)strlen(word)){
                        word[i] = '9';
                    }
                    ma = atol(word);
                    last_i = 0;
                    FE(i,cur+1,ma){
                        sprintf(word, "%d\0",i);
                        reverse(word, word + strlen(word));
                        s_cur2 = atol(word);

                        if (s_cur2 <= N && s_cur < s_cur2){
                            s_cur = s_cur2;
                            last_i = i;
                        }
                    }
                    if (last_i != 0){
                        count += last_i - cur;
                    }
                    cur = s_cur;

                    // sprintf(word, "%d\0",cur + 1);
                    // reverse(word, word + strlen(word));
                    // s_cur2 = atol(word);
                    //
                    // if (s_cur2 > cur + 2 && s_cur2 <= N && s_cur < s_cur2){
                    //     cur++;
                    // }else{
                    //     cur = s_cur;
                    // }
                }else{
                    cur++;
                }
                count++;
                if (cur == N){
                    break;
                }
            }


            // count = 11;
            // FE(i,12,N){
            //     sprintf(word, "%d\0",i);
            //     reverse(word, word + strlen(word));
            //     if (s_cur > cur + 1 && s_cur <= N){
            //         if (last.first != 0)
            //     }else{
            //
            //     }
            // }
        }




        // while(true){
        //     sprintf(word, "%d\0",cur);
        //     reverse(word, word + strlen(word));
        //     s_cur = atol(word);
        //     if (s_cur > cur + 1 && s_cur <= N){
        //         cur = s_cur;
        //     }else{
        //         cur++;
        //     }
        //     count++;
        //
        //     if (cur == N){
        //         break;
        //     }
        // }

        PR("Case #%d: %ld\n",_case_,count);
    }

    exit( EXIT_SUCCESS );
}


/*
int main( int argc, char *argv[] )
{
    LL N,count,cur,s_cur;
    char word[1000];


    CASES
    {
        SL(N);
        count = 0;
        cur = 0;

        while(true){
            sprintf(word, "%d\0",cur);
            reverse(word, word + strlen(word));
            s_cur = atol(word);
            if (s_cur > cur + 1 && s_cur <= N){
                cur = s_cur;
            }else{
                cur++;
            }
            count++;

            if (cur == N){
                break;
            }
        }

        PR("Case #%d: %ld\n",_case_,count);
    }

    exit( EXIT_SUCCESS );
}*/
