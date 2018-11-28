#include <cstdio>
#include <iostream>

#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>

#include <algorithm>
#include <functional>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef vector<vector<int> > Lawn;

bool is_good_row(const Lawn &lawn, int height, size_t row_number)
{
    size_t m = lawn[0].size();

    for(size_t i = 0; i < m; ++i)
        if(lawn[row_number][i] > height)
            return false;

    return true;
}

void cut_row(Lawn &lawn, int height, size_t row_number)
{
    if(is_good_row(lawn, height, row_number)) {
        size_t m = lawn[0].size();
        for(size_t i = 0; i < m; ++i)
            if(lawn[row_number][i] == height)
                lawn[row_number][i] = 0;
    }
}

bool is_good_column(const Lawn &lawn, int height, size_t column_number)
{
    size_t n = lawn.size();
    for(size_t i = 0; i < n; ++i)
        if(lawn[i][column_number] > height)
            return false;

    return true;
}

void cut_column(Lawn &lawn, int height, size_t column_number)
{
    if(is_good_column(lawn, height, column_number)) {
        size_t n = lawn.size();
        for(size_t i = 0; i < n; ++i)
            if(lawn[i][column_number] == height)
                lawn[i][column_number] = 0;
    }
}

void cut_height(Lawn &lawn, int height)
{
    size_t n = lawn.size();
    size_t m = lawn[0].size();

    for(size_t i = 0; i < n; ++i)
        cut_row(lawn, height, i);

    for(size_t i = 0; i < m; ++i)
        cut_column(lawn, height, i);
}

bool is_field_clean(const Lawn &lawn)
{
    for(auto &row: lawn)
        for(auto h: row)
            if(h != 0)
                return false;

    return true;
}

void solve_case(Lawn lawn, int case_number)
{
    set<int> hs;
    for(auto &row: lawn)
        for(auto h: row)
            hs.insert(h);

    for(auto h: hs)
        cut_height(lawn, h);

    cout << "Case #" << case_number << ": ";

    if(is_field_clean(lawn))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

Lawn read_case()
{
    Lawn result;
    int n, m;
    cin >> n >> m;
    result.resize(n);

    for(int i = 0; i < n; ++i) {
        result[i].resize(m);
        for(int j = 0; j < m; ++j)
            cin >> result[i][j];
    }

    return result;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    for(int i = 1; i <= t; ++i) {
        auto lawn = read_case();
        solve_case(lawn, i);
    }

    return 0;
}

// Local Variables:
// eval: (when (fboundp 'flymake-mode) (flymake-mode 1))
// End:
