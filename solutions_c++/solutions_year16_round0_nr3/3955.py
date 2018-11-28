#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<vector>
#include<cmath>
using namespace std;

int res[50], n, j, deep = 0;
long long a[50];

bool judge(long long *a)
{
    bool flag;
    for(long long i = 2; i <= 10; i++)
    {
        long long item = 0;
        flag = false;
        for(int j = 0; j < n; j++)
        {
            item *= i;
            item += a[j];
        }
        for(long long j = 2; j * j <= item; j++)
        {
            if(item % j == 0)
            {
                flag = true;
                res[i] = j;
                break;
            }
        }
        if(!flag)
            return false;
    }
    return true;
}

void dfs(int pos)
{
    if(deep == j)
        return ;
    if(pos == n - 1)
    {
        if(judge(a))
        {
            deep++;
            for(int i = 0; i < n; i++)
                cout << a[i];
            for(int i = 2; i <= 10; i++)
                cout << " " << res[i];
            cout << endl;
        }
    }
    else
    {
        a[pos] = 0;
        dfs(pos + 1);
        a[pos] = 1;
        dfs(pos + 1);
    }
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int t;
    cin >> t;
    for(int ti = 1 ; ti <= t; ti++)
    {
        printf("Case #%d:\n",ti);
        cin >> n >> j;
        deep = 0;
        a[0] = 1;
        a[n-1] = 1;
        dfs(1);
    }
    return 0;
}
