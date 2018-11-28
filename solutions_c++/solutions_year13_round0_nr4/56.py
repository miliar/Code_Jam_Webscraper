#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int N_MAX = 205, KEY_MAX = 405;

int K, N, need[N_MAX];
vector<int> inside[N_MAX];
int have[KEY_MAX];
int num_chests[KEY_MAX];
bool opened[N_MAX];
bool visited[N_MAX];
bool edge[N_MAX][N_MAX];

void initialize()
{

}

void open(int chest)
{
    assert(!opened[chest]);
    opened[chest] = true;

    if (chest < N)
    {
        assert(have[need[chest]] > 0);
        have[need[chest]]--;
    }

    for (int i = 0; i < (int) inside[chest].size(); i++)
        have[inside[chest][i]]++;
}

void unopen(int chest)
{
    assert(opened[chest]);
    opened[chest] = false;

    if (chest < N)
        have[need[chest]]++;

    for (int i = 0; i < (int) inside[chest].size(); i++)
        have[inside[chest][i]]--;
}

bool dfs(int num, int original)
{
    if (opened[num])
        return false;

    if (num == original)
        return true;

    if (visited[num])
        return false;

    visited[num] = true;

    if (original == -1)
        original = num;

    for (int i = 0; i < N; i++)
        if (edge[num][i] && dfs(i, original))
            return true;

    return false;
}

bool possible()
{
    bool copy[N_MAX];
    memcpy(copy, opened, sizeof(opened));
    bool change = true;

    while (change)
    {
        memset(num_chests, 0, sizeof(num_chests));
        change = false;

        for (int i = 0; i < N; i++)
            if (!opened[i])
                num_chests[need[i]]++;

        for (int i = 0; i < N; i++)
            if (!opened[i] && have[need[i]] >= num_chests[need[i]])
            {
                open(i);
                change = true;
            }

        memset(visited, false, sizeof(visited));

        for (int i = 0; i < N; i++)
            if (!opened[i] && (have[need[i]] > 0 && dfs(i, -1)))
            {
                open(i);
                change = true;
            }
    }

    bool answer = true;

    for (int i = 0; i < N; i++)
        if (!opened[i])
            answer = false;

    for (int i = 0; i < N; i++)
        if (opened[i] && !copy[i])
            unopen(i);

    return answer;
}

void solve_case(int test_case)
{
    scanf("%d %d", &K, &N);

    for (int i = 0; i <= N; i++)
        inside[i].clear();

    for (int i = 0; i < K; i++)
    {
        int x;
        scanf("%d", &x);
        inside[N].push_back(x);
    }

    for (int i = 0; i < N; i++)
    {
        int n;
        scanf("%d %d", &need[i], &n);

        for (int j = 0; j < n; j++)
        {
            int x;
            scanf("%d", &x);
            inside[i].push_back(x);
        }
    }

    memset(edge, false, sizeof(edge));

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < (int) inside[i].size(); k++)
                if (inside[i][k] == need[j])
                    edge[i][j] = true;

    printf("Case #%d: ", test_case);
    memset(have, 0, sizeof(have));
    memset(opened, false, sizeof(opened));
    open(N);
    vector<int> ordering;

    for (int it = 0; it < N; it++)
        for (int i = 0; i < N; i++)
            if (!opened[i] && have[need[i]] > 0)
            {
                open(i);

                if (possible())
                {
                    ordering.push_back(i);
                    break;
                }
                else
                    unopen(i);
            }

    if ((int) ordering.size() < N)
    {
        puts("IMPOSSIBLE");
        return;
    }

    for (int i = 0; i < N; i++)
        printf("%d%c", ordering[i] + 1, i < N - 1 ? ' ' : '\n');
}

int main()
{
    initialize();
    int T; scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        solve_case(tc);
        fflush(stdout);
    }

    return 0;
}
