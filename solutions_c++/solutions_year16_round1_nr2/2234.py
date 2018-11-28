#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>

using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define FOR(i,s,n) for(int i=(s);i<(n);++i)
#define REP(i,n) FOR(i,0,(n))
#define PB(x) push_back((x))
#define CLR(a,v) memset((a),(v),sizeof((a)))
typedef long long ll;

int b[55][55];
char was_r[55], was_c[55];

bool can_row(vector<int> const & a, int row)
{
    int n = SZ(a);
    REP(i,n)if(b[row][i] && b[row][i] != a[i])return false;

    return true;
}

bool can_col(vector<int> const & a, int col)
{
    int n = SZ(a);
    REP(i,n)if(b[i][col] && b[i][col] != a[i])return false;

    return true;
}



void solve()
{
    int n;
    cin>>n;

    map<int, vector<vector<int>>> m;

    int mn=999999, mx=0;

    REP(i,2*n-1)
    {
        vector<int> a(n);
        REP(i,n)cin>>a[i];

        if(a[0]<mn)mn=a[0];
        if(a.back()>mx)mx=a.back();
        m[a[0]].push_back(a);
    }


    CLR(b,0);

    if (SZ(m[mn]) == 2)
    {
        REP(i,n)b[i][0] = m[mn][0][i], b[0][i]=m[mn][1][i];
        was_r[0] = was_c[0] = 1;
    }
    else
    {
        map<int, vector<vector<int>>> mm;
        for (auto const & p : m)
        {
            for (int i = 0; i < SZ(p.second); ++i)
            {
                vector<int> a(n);
                REP(j,n)a[j]=-p.second[i][n-1-j];
                mm[a[0]].push_back(a);
            }
        }

        m.swap(mm);
        mn = -mx;

        REP(i,n)b[i][0] = m[mn][0][i], b[0][i]=m[mn][1][i];
        was_r[0] = was_c[0] = 1;
    }


    CLR(was_c, 0);
    CLR(was_r, 0);

    set<int> used1;

    int row = 0, col = 0;
    for (auto const & p : m) if (SZ(p.second) == 1)
    {
        int v = p.first;
        while(row < n && b[row][0] < v)++row;
        while(col < n && b[0][col] < v)++col;

        if (row < n && b[row][0] == v && (col == n || b[0][col] != v))
        {
            REP(i,n)b[row][i] = p.second[0][i];
            was_r[row] = 1;
            used1.insert(v);
        }
        else if (col < n && b[0][col] == v && (row == n || b[row][0] != v))
        {
            REP(i,n)b[i][col] = p.second[0][i];
            was_c[col] = 1;
            used1.insert(v);
        }
        else if (row < n && b[row][0] == v && !can_col(p.second[0], col))
        {
            REP(i,n)b[row][i] = p.second[0][i];
            was_r[row] = 1;
            used1.insert(v);
        }
        else if (col < n && b[0][col] == v && !can_row(p.second[0], row))
        {
            REP(i,n)b[i][col] = p.second[0][i];
            was_c[col] = 1;
            used1.insert(v);
        }
    }

    char was = 1;
    while(was)
    {
        was = 0;
        row = 0, col = 0;
        for (auto const & p : m) if (SZ(p.second) == 2)
        {
            int v = p.first;
            while(row < n && b[row][0] < v)++row;
            while(col < n && b[0][col] < v)++col;

            if (was_r[row] || was_c[col])continue;

            if (can_row(p.second[0], row) && !can_col(p.second[0], col))
            {
                REP(i,n)b[row][i] = p.second[0][i];
                REP(i,n)b[i][col] = p.second[1][i];
                was_r[row] = was_c[col] = 1;
                was = 1;
            }
            else if (can_row(p.second[1], row) && !can_col(p.second[1], col))
            {
                REP(i,n)b[row][i] = p.second[1][i];
                REP(i,n)b[i][col] = p.second[0][i];
                was_r[row] = was_c[col] = 1;
                was = 1;
            }
            else if (p.second[0][row] == p.second[1][col] && p.second[1][row] != p.second[0][col])
            {
                REP(i,n)b[row][i] = p.second[1][i];
                REP(i,n)b[i][col] = p.second[0][i];
                was_r[row] = was_c[col] = 1;
                was = 1;
            }
            else if (p.second[1][row] == p.second[0][col] && p.second[0][row] != p.second[1][col])
            {
                REP(i,n)b[row][i] = p.second[0][i];
                REP(i,n)b[i][col] = p.second[1][i];
                was_r[row] = was_c[col] = 1;
                was = 1;
            }
        }

        row = 0, col = 0;
        for (auto const & p : m) if (SZ(p.second) == 1)
        {
            int v = p.first;
            if (used1.count(v))continue;

            while(row < n && b[row][0] < v)++row;
            while(col < n && b[0][col] < v)++col;

            if (row < n && b[row][0] == v && (col == n || b[0][col] != v))
            {
                REP(i,n)b[row][i] = p.second[0][i];
                was_r[row] = 1;
                used1.insert(v);
                was = 1;
            }
            else if (col < n && b[0][col] == v && (row == n || b[row][0] != v))
            {
                REP(i,n)b[i][col] = p.second[0][i];
                was_c[col] = 1;
                used1.insert(v);
                was = 1;
            }
            else if (row < n && b[row][0] == v && !can_col(p.second[0], col))
            {
                REP(i,n)b[row][i] = p.second[0][i];
                was_r[row] = 1;
                used1.insert(v);
                was = 1;
            }
            else if (col < n && b[0][col] == v && !can_row(p.second[0], row))
            {
                REP(i,n)b[i][col] = p.second[0][i];
                was_c[col] = 1;
                used1.insert(v);
                was = 1;
            }
        }

        if (was)continue;

        row = 0, col = 0;
        for (auto const & p : m) if (SZ(p.second) == 2)
        {
            int v = p.first;
            while(row < n && b[row][0] < v)++row;
            while(col < n && b[0][col] < v)++col;

            if (was_r[row] || was_c[col])continue;

            REP(i,n)b[row][i] = p.second[0][i];
            REP(i,n)b[i][col] = p.second[1][i];
            was_r[row] = was_c[col] = 1;
            was = 1;
            break;
        }
    }

    row = 0, col = 0;
    for (auto const & p : m) if (SZ(p.second) == 1)
    {
        int v = p.first;
        if (used1.count(v))continue;

        while(row < n && b[row][0] < v)++row;
        while(col < n && b[0][col] < v)++col;

        if (row < n && b[row][0] == v)
        {
            REP(i,n)b[row][i] = p.second[0][i];
            was_r[row] = 1;
            used1.insert(v);
        }
        else if (col < n && b[0][col] == v)
        {
            REP(i,n)b[i][col] = p.second[0][i];
            was_c[col] = 1;
            used1.insert(v);
        }
    }

    vector<int> res(n);


    REP(i,n)if(!was_r[i])
    {
        REP(j,n)res[j] =  b[i][j];

        if(res[0] < 0)
        {
            reverse(ALL(res));
            REP(j,n)res[j]=-res[j];
        }
        REP(j,n)cout << res[j] << " ";
        cout << endl;
        return;
    }

    REP(i,n)if(!was_c[i])
    {
        REP(j,n)res[j] = b[j][i];
        if(res[0] < 0)
        {
            reverse(ALL(res));
            REP(j,n)res[j]=-res[j];
        }
        REP(j,n)cout << res[j] << " ";
        cout << endl;
        return;
    }

    cout << "Error!\n";
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    freopen("../data/B-small-attempt1.in", "r", stdin);
    freopen("../output.txt", "w+", stdout);

    int T;
    scanf("%d", &T);
    REP(i, T)
    {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
