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
const double EPS = 1e-9;
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
    //freopen(PROBLEM_ID".in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        int n;
        cin >> n;
        vector<int> a(n);
        int y = 0, z = 0, maxdiff = 0;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            if (i > 0 && a[i] < a[i - 1]) {
                int diff = a[i - 1] - a[i];
                y += diff;
                maxdiff = max(diff, maxdiff);
            }
        }

        for (int j = 0; j < n - 1; j++) {
            z += min(maxdiff, a[j]);
        }

        cout << "Case #" << test << ": " << y << " " << z << endl;
    }
    //printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}
