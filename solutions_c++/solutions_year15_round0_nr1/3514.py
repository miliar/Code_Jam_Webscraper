#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <climits>
#include <fstream>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <functional>
#include <iterator>
#include <complex>
#include <queue>
#include <cassert>
#include <sstream>
#include <cstdlib>

#define PROBLEM_ID ""

using namespace std;

double pi = acos((double) -1);
const int MOD = 1000000007;
const int INF = 2147483647;
const long long LLONG_INF = 9223372036854775807LL;

template<typename T>
void print(vector<T>& a) {
    for (int i = 0; i < a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    clock_t tStart = clock();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        int n;
        cin >> n;
        int standing_count = 0;
        int answer = 0;
        for (int i = 0; i < n + 1; i++) {
            char c;
            cin >> c;
            int digit = c - '0';
            if (i > standing_count) {
                answer += i - standing_count;
                standing_count += i - standing_count;
            }
            standing_count += digit;
        }
        cout << "Case #" << test << ": " << answer << endl;
    }
    //printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}
