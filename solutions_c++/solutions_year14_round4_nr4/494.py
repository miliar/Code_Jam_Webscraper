#include <iostream>
#include <string>
#include <set>

#define M 1010

using namespace std;

string a[M];
int assignment[M];

int test(int m, int n)
{
    int ret = 0;
    for (int i = 0; i < n; ++i)
    {
        set<string> prefix;
        for (int j = 0; j < m; ++j)
        {
            if (assignment[j] == i)
            {
                for (int k = 0; k <= a[j].length(); ++k)
                    prefix.insert(a[j].substr(0, k));
            }
        }
        ret += prefix.size();
    }
    return ret;
}

bool exist[101];
bool valid(int m, int n)
{
    memset(exist, false, sizeof(exist));
    for (int i = 0; i < m; ++i)
        exist[assignment[i]] = true;
    for (int i = 0; i < n; ++i)
        if (!exist[i])
            return false;
    return true;
}

int worst, worst_count;
void solve(int pos, int m, int n)
{
    if (pos == m)
    {
        if (valid(m, n))
        {
            int t = test(m, n);
            if (t > worst)
            {
                worst = t;
                worst_count = 1;
            }
            else if (t == worst)
                ++worst_count;
        }
        return;
    }
    for (int i = 0; i < n; ++i)
    {
        assignment[pos] = i;
        solve(pos + 1, m, n);
    }
}

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        cout << cs << endl;
        int m, n;
        cin >> m >> n;
        for (int i = 0; i < m; ++i)
            cin >> a[i];

        worst = 0;
        worst_count = 0;
        solve(0, m, n);
        cout << "Case #" << cs << ": " << worst << " " << worst_count << endl;
    }
    return 0;
}
