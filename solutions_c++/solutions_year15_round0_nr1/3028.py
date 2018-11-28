#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
using namespace std;

//--------------------------------------------
#define SZ(x) ((int)x.size())
#define pb(x) push_back(x)
#define mp(a, b) make_pair(a, b)
#define ALL(X) X.begin(), X.end()
#define SRT(x) sort(ALL(x))
#define RVRS(x) reverse(ALL(x))
#define FILL(x, value) memset(x, value, sizeof(x))

#define next next1
#define hash hash1
#define rank rank1

#ifdef _DEBUG_
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

#if((_WIN32 || __WIN32__) && __cplusplus < 201103L)
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

template <class T> inline void check_max(T& actual, T check) {
    if(actual < check) {
        actual = check;
    }
}

template <class T> inline void check_min(T& actual, T check) {
    if(actual > check) {
        actual = check;
    }
}   

const double EPS = 1e-9;
const int IINF = 1000000000;
const double PI = acos(-1.0);
const long long LINF = 6000000000000000000LL;
//--------------------------------------------

namespace Solution {

const int maxN = 1007;

int foo;
char S[maxN];

void cleanup() {

}

bool Read() {
    cleanup();
    if(scanf("%d %s", &foo, S) == 2) {
        return true;
    }
    return false;
}

void Run() {
    int n = strlen(S);
    int need = 0, already = 0;
    for(int i = 0; i < n; ++i) {
        int num = S[i] - '0';
        if(num == 0) continue;
        if(i <= already) {
            already += num;
        }
        else {
            need += i - already;
            already += i - already + num;
        }
    }
    printf("%d\n", need);
}

} // Solution

namespace StressTest {

long long GetTime() {
#ifdef __GNUC__ 
    long long res; 
    asm volatile ("rdtsc" : "=A" (res)); 
    return res;
#else
    int low, hi; 
    __asm { 
        rdtsc
        mov low, eax
        mov hi, edx
    }
    return (((long long)hi) << 32LL) | low;
#endif
}

void GenerateInput() {
    FILE* output = fopen("input.txt", "w");
    srand(GetTime());

    fclose(output);
}

void BruteForce() {
    FILE* input = fopen("input.txt", "r");
    FILE* output = fopen("brute.out", "w");

    fclose(input);
    fclose(output);
}

} // StressTest

int main() {
#ifdef _DEBUG_
//    StressTest::GenerateInput();
//    StressTest::BruteForce();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int test_cases;
    scanf("%d", &test_cases);
    for(int test_id = 1; test_id <= test_cases; ++test_id) {
#ifdef _DEBUG_
        clock_t startTime = clock();
        eprintf("Begin of test #%d:\n", test_id);
#endif

        printf("Case #%d: ", test_id);
        Solution::Read();
        Solution::Run();

#ifdef _DEBUG_
        clock_t endTime = clock();
        eprintf("Time consumed for test #%d is %lf\n", test_id, (double)(endTime - startTime) / (double)CLOCKS_PER_SEC);
#endif
    }
    return 0;
}
