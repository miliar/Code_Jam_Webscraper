
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

string solve(const vector<vector<int> >& b, int N, int M)
{
    vector<int> row_max(N, -1);
    vector<int> col_max(M, -1);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            row_max[i] = max(row_max[i], b[i][j]);
            col_max[j] = max(col_max[j], b[i][j]);
        }
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            int m = min(row_max[i], col_max[j]);
            if (m != b[i][j]) return "NO";
        }
    }
    return "YES";
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 0; t < T; ++t) {
        int N;
        scanf("%d", &N);
        int M;
        scanf("%d", &M);
        vector<vector<int> > b(N, vector<int>(M));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                int x;
                scanf("%d", &x);
                b[i][j] = x;
            }
        }

        printf("Case #%d: %s\n", t+1, solve(b, N, M).c_str());
    }
}

