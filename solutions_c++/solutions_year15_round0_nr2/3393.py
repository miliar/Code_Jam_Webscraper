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
const int MAXN = 1000;

int dp[MAXN+5][MAXN+5];

template<typename T>
void print(vector<T>& a) {
    for (int i = 0; i < a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
}

void random_shuffle(deque<int>& a) {
    for (int j = a.size() - 1; j > 0; j--) {
        int i = rand() % (j + 1);
        swap(a[i], a[j]);
    }
}

int partition(deque<int>& a, int lo, int hi) {
    int i = lo, j = hi + 1;
    int v = a[lo];

    while (true) {
        while (a[++i] > v) {
            if (i == hi)
                break;
        }

        while (a[--j] < v) {
            if (j == lo)
                break;
        }

        if (i >= j)
            break;

        swap(a[i], a[j]);
    }

    swap(a[lo], a[j]);

    return j;
}

void quicksort(deque<int>& a, int lo, int hi) {
    if (lo >= hi)
        return;
    int j = partition(a, lo, hi);
    quicksort(a, lo, j-1);
    quicksort(a, j+1, hi);
}

void quicksort(deque<int>& a) {
    random_shuffle(a);
    quicksort(a, 0, a.size() - 1);
}

/*struct Heap {*/
    //vector<int> pq;
    //int size = 0;

    //Heap(int maxn) {
        //pq.resize(maxn + 9, -1);
    //}

    //void insert(int v) {
        //pq[++size] = v;
        //swim(size);
    //}

    //int del_max() {
        //int m = pq[1];
        //swap(pq[1], pq[size--]);
        //pq[size+1] = -1;
        //sink(1);
        //return m;
    //}

    //int get_max() {
        //return pq[1];
    //}

    //void swim(int v) {
        //while (v > 1 && pq[v/2] < pq[v]) {
            //swap(pq[v/2], pq[v]);
            //v/=2;
        //}
    //}

    //void sink(int v) {
        //while (2*v <= size) {
            //int j = 2*v;
            //if (j < size && pq[j] < pq[j+1])
                //j++;
            //if (pq[v] >= pq[j])
                //break;
            //swap(pq[v], pq[j]);
            //v = j;
        //}
    //}
/*};*/

double p_EPS = pow(10, 9);
double my_round(double d) {
    double res = floor(d * p_EPS + 0.5) / p_EPS;
    return res;
}

int get_dp(int from, int to) {
    if (from <= to)
        return 0;
    if (dp[from][to] != INF)
        return dp[from][to];
    for (int k = 1; k <= from / 2; k++) {
        dp[from][to] = min(dp[from][to], get_dp(k, to) + get_dp(from - k, to) + 1);
    }
    return dp[from][to];
}

int main() {
    srand(time(0));
    ios_base::sync_with_stdio(0);
    clock_t tStart = clock();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int i = 0; i < MAXN + 5; i++) {
        for (int j = 0; j < MAXN + 5; j++) {
            dp[i][j] = INF;
        }
    }

    for (int test = 1; test <= tests; test++) {
        int n;
        cin >> n;
        deque<int> d(n);
        int total_pancakes = 0;
        for (int i = 0; i < n; i++) {
            cin >> d[i];
            total_pancakes += d[i];
        }

        quicksort(d);

        int max_pi = d[0];
        int maxminutes = max_pi;
        for (int time = 2; time < max_pi; time++) {
            int answer = 0;
            for (int i = 0; i < d.size(); i++) {
                if (d[i] <= time)
                    break;
                answer += get_dp(d[i], time);
            }

            maxminutes = min(maxminutes, answer + time);
        }

        cout << "Case #" << test << ": " << maxminutes << endl;
    }
    //printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}
