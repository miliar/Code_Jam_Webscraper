#include <vector>
#include <stack>
#include <algorithm>
#include <cstdio>

using namespace std;

void assign(int base, const vector<vector<bool> >& edges, const vector<int>& vs, vector<int>& ans)
{
    int n = (int)vs.size();
    vector<bool> visited(n, false);
    stack<int> s;
    for (int i = 0; i < n; ++i)
    {
        if (visited[i])
            continue;
        s.push(i);
        vector<int> smaller;
        while (!s.empty())
        {
            int t = s.top();
            s.pop();
            if (visited[t])
                continue;
            visited[t] = true;
            if (t != i)
                smaller.push_back(vs[t]);
            for (int j = 0; j < n; ++j)
            {
                if (edges[vs[j]][vs[t]])
                    s.push(j);
            }
        }
        sort(smaller.begin(), smaller.end());
        ans[vs[i]] = base + (int)smaller.size();
        assign(base, edges, smaller, ans);
        base = ans[vs[i]] + 1;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        scanf("%d", &N);
        vector<int> A(N);
        for (int i = 0; i < N; ++i)
            scanf("%d", &A[i]);
        vector<int> B(N);
        for (int i = 0; i < N; ++i)
            scanf("%d", &B[i]);
        vector<vector<bool> > edges(N);
        for (int i = 0; i < N; ++i)
            edges[i].assign(N, false);
        for (int i = 0; i < N; ++i)
        {
            for (int j = i + 1; j < N; ++j)
            {
                if (A[i] >= A[j])
                    edges[j][i] = true;
                if (B[i] <= B[j])
                    edges[i][j] = true;
            }
        }
        vector<int> last(N + 1);
        for (int i = 0; i < N; ++i)
        {
            if (A[i] > 1)
                edges[last[A[i] - 1]][i] = true;
            last[A[i]] = i;
        }
        for (int i = N - 1; i >= 0; --i)
        {
            if (B[i] > 1)
                edges[last[B[i] - 1]][i] = true;
            last[B[i]] = i;
        }
        vector<int> vs(N);
        for (int i = 0; i < N; ++i)
            vs[i] = i;
        vector<int> ans(N);
        assign(1, edges, vs, ans);
        printf("Case #%d:", testcase);
        for (int i = 0; i < N; ++i)
            printf(" %d", ans[i]);
        putchar('\n');
    }
}
