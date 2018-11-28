#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }

const int MAXV = 2048, MAXE = MAXV * MAXV;
int E, ptr[MAXV], next[MAXE], adj[MAXE], ord[MAXV];
set<pair<int, int> > es;

void topsort_sub(int u, int& cur)
{
    vector<int> nexts;
    for (int z = ptr[u]; ~z; z = next[z]) {
        int v = adj[z];
        nexts.push_back(v);
    }
    sort(nexts.begin(), nexts.end());

    for (int i = 0; i < nexts.size(); ++i) {
        if (!~ord[nexts[i]]) {
            topsort_sub(nexts[i], cur);
        }
    }

    ord[u] = cur;
    ++cur;
}

void lexfirst_topsort(int n)
{
    int cur = 0;
    memset(ord, ~0, sizeof(ord));
    for (int i = 0; i < n; ++i) {
        if (!~ord[i]) {
            topsort_sub(i, cur);
        }
    }
}

void add_edge(int u, int v)
{
    swap(u, v);
    if (es.find(make_pair(u, v)) != es.end()) return;
    es.insert(make_pair(u, v));
    next[E] = ptr[u]; ptr[u] = E; adj[E] = v; ++E;
}

int main()
{
    int T;
    cin >> T;

    for (int CN = 1; CN <= T; ++CN) {
        int N;
        cin >> N;

        int A[2048], B[2048];
        for (int i = 0; i < N; ++i) {
            cin >> A[i];
        }
        for (int i = 0; i < N; ++i) {
            cin >> B[i];
        }

        es.clear();
        memset(ptr, ~0, sizeof(ptr));
        E = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < i; ++j) {
                if (A[j] >= A[i]) {
                    add_edge(i, j);
                }
            }
            for (int j = i + 1; j < N; ++j) {
                if (B[j] >= B[i]) {
                    add_edge(i, j);
                }
            }
            for (int j = i - 1; j >= 0; --j) {
                if (A[j] == A[i] - 1) {
                    add_edge(j, i);
                    break;
                }
            }
            for (int j = i + 1; j < N; ++j) {
                if (B[j] == B[i] - 1) {
                    add_edge(j, i);
                    break;
                }
            }
        }

        lexfirst_topsort(N);

        cout << "Case #" << CN << ":";
        for (int i = 0; i < N; ++i) {
            cout << " " << ord[i] + 1;
        }
        cout << endl;
    }

    return 0;
}
