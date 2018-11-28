#include <stdio.h>
#include <assert.h>
#include <string.h>

#include <iostream>
#include <vector>
#include <bitset>
#include <map>
#include <unordered_map>

#include <time.h>
#include <stdlib.h>     /* srand, rand */


// These are portable on both x86 and x64 compilers
typedef short int i16;
typedef short unsigned u16;
typedef int i32;
typedef unsigned int u32;

//!!!!TODO
// From https://stackoverflow.com/questions/152016/detecting-cpu-architecture-compile-time
//#ifdef __i386__

// These are for x86 compilers
typedef long long int i64;
typedef long long unsigned u64;


#ifndef __i386__
/*
// These are for x64 compilers
typedef long i64;
typedef long unsigned u64;
typedef long long int i128;
typedef long long unsigned u128;
*/
#endif

using namespace std;







// From https://stackoverflow.com/questions/15240/how-do-you-create-a-debug-only-function-that-takes-a-variable-argument-list-lik

//#define MY_DEBUG


#ifdef MY_DEBUG
    #define dout cout
    // See http://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
    #define dprintf(...) printf(__VA_ARGS__)
#else
    #define dout 0 && cout
    #define dprintf(...) 0 && printf(__VA_ARGS__)
#endif


/*
int debug_printf( const char *fmt, ... );
#if defined( MY_DEBUG )
  #define DEBUG_PRINTF(x) debug_printf x
#else
   #define DEBUG_PRINTF(x)
#endif

//DEBUG_PRINTF(( "Format string that takes %s %s\n", "any number", "of args" ));
*/


int T, N;

/*
1 <= T <= 100
1 <= N <= 150
2 <= L <= 40
*/

#define T_MAX 100
//#define NMAX 1001
#define NMAX 11

#define STRLEN_MAX 30






FILE *fin;





int degree[NMAX];
//int edges[NMAX];
vector<pair<int, int>> edgeList;
int edgesNode[NMAX][2];

int Solve(int numTestCase) {
    int i, j;
    int res = 0;

  #ifdef MY_DEBUG
    for (i = 0; i < N; i++) {
        printf("degree[%d] = %d\n", i, degree[i]);
    }
    dprintf("Nodes with 2-degree: ");
    for (i = 0; i < N; i++) {
        if (degree[i] == 2)
            dprintf("%d ", i);
    }
    dprintf("\n");
    dprintf("Nodes with 3-degree: ");
    for (i = 0; i < N; i++) {
        if (degree[i] == 3)
            dprintf("%d ", i);
    }
    dprintf("\n");
  #endif

    for (i = 0; i < 0; i++) {
        if (degree[i] == 1)
            // We remove node i
            res++;
            //edgesNode[]
    }

    return res;
    //return -1234;
}



void ReadData() {
    int i, j;
    char str[STRLEN_MAX + 1];
    int numTestCase;
    int v1, v2;
    int A, B, K;
    int a, b, aband, sol;

    //printf("fin = %p\n", fin);

    fscanf(fin, "%d\n", &T);
    assert((T >= 1) && (T <= T_MAX));

    //printf("T = %d\n", T);

    for (numTestCase = 1; numTestCase <= T; numTestCase++) {
        /*
        fgets(str, STRLEN_MAX, fin);
        sscanf(str, "%d", &N);
        */
        fscanf(fin, "%d%d%d", &A, &B, &K);
        dprintf("A = %d, B = %d, K = %d\n", A, B, K);

        sol = 0;
        for (a = 0; a < A; a++) {
            for (b = 0; b < B; b++) {
                aband = a & b;
                if (aband < K) {
                    sol++;
                }
            }
        }

        printf("Case #%d: %d\n", numTestCase, sol);

        continue;

        int res = Solve(numTestCase);

        /*
        if (res == -1234)
            printf("Case #%d: NOT POSSIBLE\n", numTestCase);
        else
            printf("Case #%d: %d\n", numTestCase, res);
        */
        fflush(stdout);



        edgeList.clear();
        //return;
    }
}


int main() {
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A.in", "rt", stdin);
    //freopen("A-large-practice.in", "rt", stdin);
    //freopen("Z:\\1Job_Search\\Google\\Google_CodeJAM_2009\\Online_Round_1\\C\\A-large-practice.out", "wt", stdout);

    //freopen("A.in", "rt", stdin);
    //freopen("A_orig.in", "rt", stdin);
    //freopen("A-small-attempt2.in", "rt", stdin);
    //freopen("A-large.in", "rt", stdin);
    //freopen("A-small.in", "rt", stdin);
    freopen("B-small-attempt0.in", "rt", stdin);
    //freopen("A.out", "wt", stdout);

    //printf("%lld\n", std::bitset<40>("100000000000000000000000000000000000").to_ullong());


    fin = stdin;
    ReadData();

    fclose(fin);

    return 0;
}
