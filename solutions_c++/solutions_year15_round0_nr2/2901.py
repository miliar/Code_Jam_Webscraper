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

int n, D[maxN];

void cleanup() {

}

bool Read() {
    cleanup();
    if(scanf("%d", &n) == 1) {
        for(int i = 0; i < n; ++i) {
            scanf("%d", D + i);
        }
        return true;
    }
    return false;
}

void Run() {
    int answer = 0;
    for(int i = 0; i < n; ++i) {
        check_max(answer, D[i]);
    }
    int mmax = answer;
    for(int val = 1; val <= mmax; ++val) {
        int total = 0;
        for(int i = 0; i < n; ++i) {
            if(D[i] > val) {
                int rem = (D[i] % val) == 0;
                total += D[i] / val - rem;
            }
        }
        total += val;
        check_min(answer, total);
    }
    printf("%d\n", answer);
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

int n, B[10], bound;

int solve(int passed) {
    if(passed > bound) {
        return IINF;
    }
    int mmax = 0;
    for(int i = 1; i <= 9; ++i) {
        if(B[i] > 0) {
            mmax = i;
        }
    }
    mmax += passed;
    for(int k = 2; k <= 9; ++k) {
        if(B[k]) {
            for(int part = 1; part < k; ++part) {
                B[part]++;
                B[k - part]++;
                B[k]--;
                check_min(mmax, solve(passed + 1));
                B[k]++;
                B[k - part]--;
                B[part]--;
            }
        }
    }
    return mmax;
}

void BruteForce() {
    FILE* input = fopen("input.txt", "r");
    FILE* output = fopen("brute.out", "w");
    int test_cases;
    fscanf(input, "%d", &test_cases);
    for(int test_id = 1; test_id <= 1; ++test_id) {
        fscanf(input, "%d", &n);
        bound = 0;
        int x;
        FILL(B, 0);
        for(int i = 0; i < n; ++i) {
            fscanf(input, "%d", &x);
            B[x]++;
            check_max(bound, x);
        }
        fprintf(output, "Case #%d: %d\n", test_id, solve(0));
    }

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
