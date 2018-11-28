#include <cstdio>
#include <cstring>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int T, n;
int A[2000], B[2000];
vector<int> e[2000];
int inDegree[2000];
int res[2000];
int last[2001];

void setLess(int i, int j) {
    ++inDegree[j];
    e[i].push_back(j);
}

int main() {
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%d", &n);
        memset(inDegree, 0, sizeof(inDegree));
        for (int i = 0; i < n; ++i) {
            e[i].clear();
        }
        for (int i = 0; i < n; ++i) {
            scanf("%d", &A[i]);
        }
        for (int i = 0; i < n; ++i) {
            scanf("%d", &B[i]);
        }

        memset(last, -1, sizeof(last));
        for (int i = 0; i < n; ++i) {
            last[A[i]] = i;
            for (int j = 0; j < i; ++j) {
                if (A[j] >= A[i]) {
                    setLess(i, j);
                } else if (A[j] + 1 == A[i] && last[A[j]] == j) {
                    setLess(j, i);;
                }
            }
        }

        memset(last, -1, sizeof(last));
        for (int i = n - 1; i >= 0; --i) {
            last[B[i]] = i;
            for (int j = i + 1; j < n; ++j) {
                if (B[i] <= B[j]) {
                    setLess(i, j);
                } else if (B[i] == B[j] + 1 && last[B[j]] == j) {
                    setLess(j, i);
                }
            }
        }

        memset(res, -1, sizeof(res));
        set<int> q;
        for (int i = 0; i < n; ++i) {
            if (inDegree[i] == 0) {
                q.insert(i);
            }
        }
        int total = 0;
        while (!q.empty()) {
            int t = *q.begin();
            q.erase(q.begin());
            res[t] = ++total;
            for (vector<int>::const_iterator i = e[t].begin(); i != e[t].end(); ++i) {
                if (--inDegree[*i] == 0) {
                    q.insert(*i);
                }
            }
        }
        printf("Case #%d:", caseNum);
        for (int i = 0; i < n; ++i) {
            printf(" %d", res[i]);
        }
        printf("\n");
    }
    return 0;
}
