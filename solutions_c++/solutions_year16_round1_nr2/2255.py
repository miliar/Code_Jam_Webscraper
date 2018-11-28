#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;

bool myfunction (vector<int> a, vector<int> b)
{
    for (int i = 0; i < a.size(); ++ i)
    {
        if (a[i] != b[i])
        {
            return a[i] < b[i];
        }
    }
    return 0;
}

bool valid(vector<vector<int> > &x, int row, int col, bool isrow, vector<int> &y, bool missrow, int missidx)
{
    if (isrow)
    {
        for (int i = 0; i < col; ++ i)
        {
            if (!missrow && missidx == i) continue;
            if (x[row][i] != y[i]) return false;
        }
        return true;
    }
    else
    {
        for (int i = 0; i < row; ++ i)
        {
            if (missrow && missidx == i) continue;
            if (x[i][col] != y[i]) return false;
        }
        return true;
    }
}

bool dfs(int row, int col, vector<vector<int> > &x, vector<vector<int> > &a, bool isrow, int idx, int k)
{
    if (row == N && col == N)
    {
        return true;
    }
    if (isrow && row == idx) return dfs(row + 1, col, x, a, isrow, idx, k);
    if (!isrow && col == idx) return dfs(row, col + 1, x, a, isrow, idx, k);
    bool flg = false;
    if (row < N && valid(x, row, col, true, a[k], isrow, idx))
    {
        for (int i = 0; i < N; ++ i)
        {
            x[row][i] = a[k][i];
        }
        flg = dfs(row + 1, col, x, a, isrow, idx, k + 1);
        if (flg) return true;
    }
    if (col < N && valid(x, row, col, false, a[k], isrow, idx))
    {
        for (int i = 0; i < N; ++ i)
        {
            x[i][col] = a[k][i];
        }
        flg = dfs(row, col + 1, x, a, isrow, idx, k + 1);
        if (flg) return true;
    }
    return false;
}

int main()
{
    ifstream fin("B-small.in");
    ofstream fout("B-small.out");
    fin >> T;
    for (int i = 0; i < T; ++ i)
    {
        fin >> N;
        vector<vector<int> > a;
        vector<vector<int> > x;
        for (int j = 0; j < N; ++ j)
        {
            vector<int> tmp;
            for (int k = 0; k < N; ++ k)
            {
                tmp.push_back(0);
            }
            x.push_back(tmp);
        }
        for (int j = 0; j < 2 * N - 1; ++ j)
        {
            vector<int> tmp;
            for (int k = 0; k < N; ++ k)
            {
                int x;
                fin >> x;
                tmp.push_back(x);
            }
            a.push_back(tmp);
        }
        sort (a.begin(), a.end(), myfunction);
        vector<int> ans;
        if (a[0][0] == a[1][0])
        {
            for (int j = 0; j < N; ++ j)
            {
                x[0][j] = a[0][j];
                x[j][0] = a[1][j];
            }
            for (int j = 1; j < N; ++ j)
            {
//                cout << j << endl;
                if (dfs(1, 1, x, a, true, j, 2))
                {
//                    cout << "correct" << endl;
//                    for (int p = 0; p < N; ++ p)
//                    {
//                        for (int q = 0; q < N; ++ q)
//                        {
//                            cout << x[p][q] << ' ';
//                        }
//                        cout << endl;
//                    }
                    ans = x[j];
                    break;
                }
            }
            if (ans.size() == 0)
            for (int j = 1; j < N; ++ j)
            {
                cout << j << endl;
                if (dfs(1, 1, x, a, false, j, 2))
                {
                    for (int k = 0; k < N; ++ k)
                    {
                        ans.push_back(x[k][j]);
                    }
                    break;
                }
            }
        }
        else
        {
            for (int j = 0; j < N; ++ j)
            {
                x[0][j] = a[0][j];
            }
            dfs(1, 1, x, a, false, 0, 1);
            for (int k = 0; k < N; ++ k)
            {
                ans.push_back(x[k][0]);
            }
        }

        fout << "Case #" << i + 1 << ": ";
        for (int k = 0; k < N; ++ k)
        {
            fout << ans[k] << ' ';
        }
        fout << endl;
    }
    return 0;
}



