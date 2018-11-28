#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

struct MyPair
{
    MyPair(int _i, int _f)
    {
        i = _i;
        f = _f;
    }
    int i;
    int f;
};

int T, N, K;

int ans = 0;

bool myfunction (MyPair i,MyPair j) { return (i.f > j.f); }

void dfs(int k, bool *has, int *a, vector<MyPair> &p, int *circle)
{
    if (k > ans)
    {
        if (k > 1 && a[circle[k - 1]] == circle[k - 2])
            ans = k;
        else if (a[circle[k - 1]] == circle[0])
            ans = k;
    }
    if (k == N) return;
    for (int i = 0; i < N; ++ i)
    {
        if (has[p[i].i]) continue;
        if (k == 0)
        {
            circle[k] = p[i].i;
            has[p[i].i] = true;
            dfs(k + 1, has, a, p, circle);
            has[p[i].i] = false;
        }
        else
        {
            if (k > 1 && a[circle[k - 1]] == circle[k - 2])
            {
                circle[k] = p[i].i;
                has[p[i].i] = true;
                dfs(k + 1, has, a, p, circle);
                has[p[i].i] = false;
            }
            else if (a[circle[k - 1]] == p[i].i)
            {
                circle[k] = p[i].i;
                has[p[i].i] = true;
                dfs(k + 1, has, a, p, circle);
                has[p[i].i] = false;
            }
        }
    }
}

int main()
{
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
    fin >> T;
    for (int i = 0; i < T; ++ i)
    {
        fin >> N;
        int a[1001];
        int f[1001] = {};
        int circle[1001] = {};
        for (int j = 0; j < N; ++ j)
        {
            fin >> a[j];
            a[j] --;
            f[a[j]] ++;
        }
        vector<MyPair> ff;
        for (int j = 0; j < N; ++ j)
        {
            ff.push_back(MyPair(j, f[j]));
        }
        sort (ff.begin(), ff.end(), myfunction);
        for (int j = 0; j < N; ++ j)
        {
            cout << ff[j].i << ' ';
        }
        cout << endl;
        bool has[1001] = {};
        ans = 0;
        dfs(0, has, a, ff, circle);
        fout << "Case #" << i + 1 << ": ";
        fout << ans;
        fout << endl;
    }
    return 0;
}




