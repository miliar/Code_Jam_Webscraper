#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

bool check(int n_div, int n_sub, vector<int> &a)
{
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] <= n_sub)
        {
            continue;
        }
        int cur = a[i] / n_sub + (a[i] % n_sub ? 1 : 0) - 1;
        if (n_div >= cur)
        {
            n_div -= cur;
        }
        else
        {
            return false;
        }
    }
    return true;
}

int test()
{
    int n;
    scanf("%d", &n);
    vector <int> a(n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for (int i = 1; i <= 1000; i++)
    {
        bool flag = false;
        for (int j = 0; j < i; j++)
        {
            if (check(j, i - j, a))
            {
                flag = true;
                break;
            }
        }
        if (flag)
            return i;
    }
}

int main()
{
    freopen("b-large.in", "r", stdin);
    freopen("b_out.txt", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": " << test() << endl;
    }
    return 0;
}
