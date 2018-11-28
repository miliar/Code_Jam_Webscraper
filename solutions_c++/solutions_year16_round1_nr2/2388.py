#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

vector< vector<int> > pieces;
int n;

bool __cmp__(const vector<int> &a, const vector<int> &b)
{
    int k = 0;
    while (k < n && a[k] == b[k])
    {
        ++k;
    }
    if (k == n)
    {
        return false;
    }
    return a[k] < b[k];
}

int M[100][100];
bool used[200], row_used[100], col_used[100];

bool accept_pos(int v, vector<int> &a, bool flag)
{
    for(int i = 0; i < n; ++i)
        if(flag)
        {
            if(col_used[i] && M[v][i] != a[i])
                return false;
            if(!col_used[i] && v && M[v-1][i] >= a[i])
                return false;
        }
        else
        {
            if(row_used[i] && M[i][v] != a[i])
                return false;
            if(!row_used[i] && v && M[i][v-1] >= a[i])
                return false;
        }
        return true;
}

void update(int v, vector<int> &a, bool flag, bool ins)
{
    if(ins)
    {
        for(int i = 0; i < n; ++i)
            if(flag)
            {
                if(!col_used[i])
                    M[v][i] = a[i];
            }
            else
            {
                if(!row_used[i])
                    M[i][v] = a[i];
            }
    }
    else
    {
        for(int i = 0; i < n; ++i)
            if(flag)
            {
                if(!col_used[i])
                    M[v][i] = 0;
            }
            else
            {
                if(!row_used[i])
                    M[i][v] = 0;
            }
    }
}

bool dfs(int v, int r, int c, bool skipped)
{
    if(v == 2*n-1)
        return true;
    used[v] = 1;

    if(r < n && accept_pos(r, pieces[v], true))
    {
        update(r, pieces[v], true, true);
        row_used[r] = true;
        if(dfs(v+1, r+1, c, skipped))
            return true;
        row_used[r] = false;
        update(r, pieces[v], true, false);
    }

    if(!skipped && r+1 < n && accept_pos(r+1, pieces[v], true))
    {
        update(r+1, pieces[v], true, true);
        row_used[r+1] = true;
        if(dfs(v+1, r+2, c, true))
            return true;
        row_used[r+1] = false;
        update(r+1, pieces[v], true, false);
    }

    if(c < n && accept_pos(c, pieces[v], false))
    {
        update(c, pieces[v], false, true);
        col_used[c] = true;
        if(dfs(v+1, r, c+1, skipped))
            return true;
        col_used[c] = false;
        update(c, pieces[v], false, false);
    }

    if(!skipped && c+1 < n && accept_pos(c+1, pieces[v], false))
    {
        update(c+1, pieces[v], false, true);
        col_used[c+1] = true;
        if(dfs(v+1, r, c+2, true))
            return true;
        col_used[c+1] = false;
        update(c+1, pieces[v], false, false);
    }

    used[v] = 0;
    return false;
}

int main()
{
    ifstream f1("B-small-attempt1.in");
    ofstream f2("B-small-attempt1.out");
    int T;
    f1 >> T;
    vector<int> in_piece;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ":";
        f1 >> n;
        in_piece.resize(n);
        pieces.resize(0);
        for(int i = 0; i < 2*n-1; ++i)
        {

            for(int j = 0; j < n; ++j)
                f1 >> in_piece[j];
            pieces.push_back(in_piece);
        }
        sort(pieces.begin(), pieces.end(), __cmp__);
        memset(used, false, sizeof used);
        memset(row_used, false, sizeof used);
        memset(col_used, false, sizeof used);
        memset(M, 0, sizeof M);
        dfs(0, 0, 0, false);
        bool flag;
        int v;
        for(int i = 0; i < n; ++i)
        {
            if(!row_used[i])
            {
                v = i;
                flag = true;
            }
            if(!col_used[i])
            {
                v = i;
                flag = false;
            }
        }
        for(int i = 0; i < n; ++i)
            if(flag)
                f2 << ' ' << M[v][i];
            else
                f2 << ' ' << M[i][v];
        f2 << endl;
    }
    return 0;
}

