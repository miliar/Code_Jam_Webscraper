#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <deque>
#include <list>
#include <algorithm>
#include <numeric>
#include <queue>
#include <set>
#include <functional>
#include <cstring>
#include <stdio.h>
#include <ctype.h>
#include <assert.h>

#define max3(x, y, z) max((x), max((y), (z)))
#define max4(w, x, y, z) max(max((x), (y)), max((z), (w)))
#define min3(x, y, z) min((x), min((y), (z)))
#define min4(w, x, y, z) min(min((x), (y)), min((z), (w)))

using namespace std;

struct UnionFind {
    vector<int> data;
    UnionFind(int size) : data(size, -1) { }
    bool unionSet(int x, int y) {
        x = root(x); y = root(y);
        if (x != y) {
            if (data[y] < data[x]) swap(x, y);
            data[x] += data[y]; data[y] = x;
        }
        return x != y;
    }
    bool findSet(int x, int y) {
        return root(x) == root(y);
    }
    int root(int x) {
        return data[x] < 0 ? x : data[x] = root(data[x]);
    }
    int size(int x) {
        return -data[root(x)];
    }
};

typedef int Weight;
struct Edge {
    int src, dst;
    Weight weight;
    Edge(int src, int dst, Weight weight) :
        src(src), dst(dst), weight(weight) { }
};

bool operator < (const Edge &e, const Edge &f) {
    return e.weight != f.weight ? e.weight > f.weight : // !!INVERSE!!
    e.src != f.src ? e.src < f.src : e.dst < f.dst;
}

typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
typedef vector<Weight> Array;
typedef vector<Array> Matrix;
typedef long long ll;
typedef unsigned long long ull;

#define FOR(i, N) for (int i = 0; i < N; i++)
#define RFOR(i, N) for (int i = N - 1; i >= 0; i--)
#define REP(i, from, to) for (int i = from; i <= to; i++)
#define MP(x, y) make_pair((x), (y))

// ワーシャルフロイド(g ... 無効間はINFが必要)
void shortestPath(const Matrix &g, Matrix &dist) {
    int n = g.size();
    dist = g;
    //inter.assign(n, vector<int>(n, -1));
    FOR(k, n) FOR(i, n) FOR(j, n) {
        if (dist[i][j] > dist[i][k] + dist[k][j]) {
            dist[i][j] = dist[i][k] + dist[k][j];
            //inter[i][j] = k;
        }
    }
}

/////////////////////////////////////////////////////////////////////////////////////////

int N, T;
int ans;

bool ok(const vector<int>& A, int N) {
    bool asc = true;
    int i = 0;
    for (; i < N - 1; i++) {
        if (A[i] > A[i + 1]) {
            asc = false;
            break;
        }
    }

    for (; i < N - 1; i++) {
        if (A[i] < A[i + 1]) return false;
    }

    return true;
}

int num_sort(int *A, int n) {
    if (n <= 1) return 0;

    int min_elem = *min_element(A, A + n);
    int c = 0;

    FOR(i, n) {
        if (A[i] == min_elem) {
            for (int j = i; j >= 1; j--) {
                A[j] = A[j - 1];
            }
            c = i;
            break;
        }
    }
    return c + num_sort(A + 1, n - 1);
}

int solve(vector<int> A, int N, int m) {

    vector<int> T(N, 0);

    int pivot = *max_element(A.begin(), A.end());

    int cost_pv;
    FOR(i, N) {
        if (A[i] == pivot) {
            cost_pv = abs(i - m);
            break;
        }
    }

    vector<int> B, C;

    FOR(i, N) {
        if (A[i] == pivot) continue;
        if (B.size() >= m) C.push_back(A[i]);
        else B.push_back(A[i]);
    }
    reverse(C.begin(), C.end());

    int cost = cost_pv;
    if (!B.empty()) cost += num_sort(&B[0], B.size());
    if (!C.empty()) cost += num_sort(&C[0], C.size());
    return cost;
}

int solve(const vector<int>& A, int N) {
    int res = 10000000;

    FOR(i, N) {
        res = min(res, solve(A, N, i));
    }
    return res;
}
/*
int main(void) {
    cin >> T;

    FOR(i, T) {
        cin >> N;

        vector<int> A(N);
        FOR(j, N) cin >> A[j];

        printf("Case #%d: %d\n", i + 1, solve(A, N));
    }
   
}
*/

struct node {
    node() : c(0) {}
    char c;
    map<char, node> next;
};

bool operator == (const node& n, char c) {
    return n.c == c;
}

struct tree {
    node n;
};

void add(const string& s, tree& t, int& size)
{
    node *pn = &t.n;

    FOR(i, s.length()) {
        if (pn->next.find(s[i]) == pn->next.end()) {
            pn->next[s[i]].c = s[i];
            size++;
        }
        pn = &pn->next[s[i]];
    }
}

int num_trie(const vector<string>& dic)
{
    tree t;
    int size = 0;
    FOR(i, dic.size()) {
        add(dic[i], t, size);
    }
    return size + 1;
}

pair<int, int> solve(const vector<string>& dic, int M, int N) {
    // try all case (4^8)
    vector<int> sv(M, 0);
    int d[5] = {M, 0, 0, 0, 0};
    map<int, int> res;
    int max_num = 0;

    goto first;
    while (1) {
        next:

        sv[0]++; d[sv[0] - 1]--; d[sv[0]]++;

        if (sv[0] == N) {
            int j = 0;
            while (1) {
                if (j == M - 1) {
                    goto end;
                }
                sv[j] = 0; d[0]++; sv[j + 1]++; d[sv[j + 1] - 1]--; d[sv[j + 1]]++;
                j++;
                if (sv[j] < N) break;
            }
        }

        first:

        FOR(i, N) {
            if (d[i] == 0) goto next;
        }

        vector<vector<string> > s(N);
        FOR(i, M) {
            s[sv[i]].push_back(dic[i]);
        }

        int num = 0;
        FOR(i, N) {
            num += num_trie(s[i]);
        }
        max_num = max(max_num, num);
        res[num]++;
    }
end:

    return MP(max_num, res[max_num]);
}

int main(void) {
    int T;
    cin >> T;

    FOR(i, T) {
        int M, N;
        scanf("%d %d\n", &M, &N);

        vector<string> dic(M);
        FOR(j, M) {
            getline(cin, dic[j]);
        }
        pair<int, int> r = solve(dic, M, N);
        printf("Case #%d: %d %d\n", i + 1, r.first, r.second);
    }
}

