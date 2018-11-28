#include <iostream>
#include <stdio.h>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <time.h>
#include <cassert>
#include <map>
#include <set>
#include <stack>
#include <time.h>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <bitset>


//#include <unordered_map>
//#include <unordered_set>

#define llong long long int
#define pb push_back
#define mp make_pair
#define pr pair <int, int>
#define X first
#define Y second
#define endl "\n"
using namespace std;
const int MAXN = 2e5 + 7;
const int INF = 1e9 + 7;
const llong LINF = 1e18;
//const llong MOD = 1e9 + 7;
//const long double EPS = 1e-18;
using namespace std;

int tests;
int used[20];

int main() {
#ifdef DEBUG
    double beg = clock();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //freopen(".in", "r", stdin);
    //freopen(".out", "w", stdout);
#endif
    //ios_base::sync_with_stdio(0);cin.tie();
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        int cur;
        scanf("%d", &cur);
        int C = 0;
        if (!cur) {
            printf("Case #%d: INSOMNIA\n", test);
            continue;
        }
        
        for (int j = 1; ; j++) {
            int x = cur * j;
            while (x) {
                int tmp = x % 10;
                if (used[tmp] != test) {
                    used[tmp] = test;
                    C++;
                }
                x /= 10;
            }
            if (C == 10) {
                printf("Case #%d: %d\n", test, cur * j);
                break;
            }
        }
    }
    
    
#ifdef DEBUG
    double end = clock();
    fprintf(stderr, "\n*** Total time = %.3lf ***\n", (end - beg) / CLOCKS_PER_SEC);
#endif
    return 0;
}