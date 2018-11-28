#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

const long long modulo = 1000000007;

size_t number(char c)
{
    return (c - 'a');
}

void dfs(size_t n, size_t v, const vector<vector<char> >& matrix,
    vector<char>* col, bool* bad)
{
    col->at(v) = 1;
    for (size_t i = 0; i < n; ++i)
    if (matrix[v][i] == 1 && col->at(i) == 0)
    {
        dfs(n, i, matrix, col, bad);
    }
    else
    if (matrix[v][i] == 1 && col->at(i) == 1)
    {
        *bad = true;
    }

    col->at(v) = 2;
}

bool check(int n, const vector<string>& data)
{
    vector<vector<char> > matrix(26, vector<char>(26, 0));
    for (size_t i = 0; i < n; ++i)
    {
        for (size_t j = 0; (j + 1) < data[i].size(); ++j)
        if (data[i][j] != data[i][j + 1])
        {
            matrix[number(data[i][j])][number(data[i][j + 1])] = 1;
        }
    }

    vector<char> col(26, 0);
    bool bad = false;
    for (size_t i = 0; i < 26; ++i)
    if (col[i] == 0) {
        dfs(26, i, matrix, &col, &bad);
    }

    return !bad;
}

bool check_order(int n, const vector<string>& data, 
    const vector<int>& order)
{
    vector<char> was(26, 0);
    for (size_t i = 0; i < n; ++i)
    {
        if (i == 0) {
            for (size_t j = 0; j < data[order[i]].size(); ++j)
            {
                was[number(data[order[i]][j])] = 1;
            }
        } 
        else
        {
            for (size_t j = 0; j < data[order[i]].size(); ++j) {
                size_t index = order[i];
                size_t p_index = order[i - 1];
                if (was[number(data[index][j])] == 1 &&
                    ((j == 0 && data[p_index][data[p_index].size() - 1] != data[index][0]) ||
                    (j != 0 && data[index][j - 1] != data[index][j])))
                {
                    return false;
                }
                else
                {
                    was[number(data[index][j])] = 1;
                }
            }
        }

    }

    return true;
}

long long rec(int n, int k, const vector<string>& data,
    vector<char>& was, vector<int>& order)
{
    if (k == n) {
        if (check_order(n, data, order))
            return 1;
        else
            return 0;
    }

    long long ans = 0;
    for (size_t i = 0; i < n; ++i)
    if (was[i] == 0) {
        was[i] = 1;
        order[k] = i;
        ans += rec(n, k + 1, data, was, order);
        ans %= modulo;
        was[i] = 0;
    }

    return ans;
}

string solution(int n, const vector<string>& data)
{
    vector<char> was(n, 0);
    vector<int> order(n);
    return to_string(rec(n, 0, data, was, order));
}

int main()
{
    ifstream cin("B-small-attempt1.in");
    ofstream cout("B-small-attempt1.out");

    int test_count;
    cin >> test_count;
    for (size_t test = 0; test < test_count; ++test)
    {
        int n;
        cin >> n;
        vector<string> data;
        for (size_t i = 0; i < n; ++i)
        {
            string line;
            cin >> line;
            data.push_back(line);
        }

        if (!check(n, data)) {
            cout << "Case #" << to_string(test + 1) << ": " << "0" << endl;
            continue;
        }

        cout << "Case #" << to_string(test + 1) << ": " << solution(n, data) << endl;
        
    }
}
