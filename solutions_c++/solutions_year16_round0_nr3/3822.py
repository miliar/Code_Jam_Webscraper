#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
int n, l;
vector<string> ans;
void prin(string cur)
{
    for(int k = 2; k <= 10; k++)
    {
        long long temp = 1;
        long long sum = 0;
        for(int i = n - 1; i >= 0; i--)
        {
            sum += (cur[i] - '0') * temp;
            temp *= k;
        }
        for(int i = 2; i <= sqrt(sum); i++)
        {
            if(sum % i == 0)
            {
                printf(" %d", i);
                break;
            }
        }
    }
}
bool work(string cur)
{
    int cnt = 0;
    for(int k = 2; k <= 10; k++)
    {
        long long temp = 1;
        long long sum = 0;
        for(int i = n - 1; i >= 0; i--)
        {
            sum += (cur[i] - '0') * temp;
            temp *= k;
        }
        for(int i = 2; i <= sqrt(sum); i++)
        {
            if(sum % i == 0)
            {
                cnt++;
                break;
            }
        }
    }
    if(cnt == 9)
        return true;
}
void dfs(string cur, int len)
{
    if(ans.size() == l)
        return ;
    if(len == n - 1)
    {
        cur += '1';
        if(work(cur))
            ans.push_back(cur);
        return ;
    }
    if(ans.size() == l)
        return ;
    dfs(cur + '1', len + 1);
    if(ans.size() == l)
        return ;
    dfs(cur + '0', len + 1);
}
int main()
{
    freopen("e.in", "r", stdin);
    freopen("e.out", "w", stdout);
    int t;
    cin >> t;
    int cas = 1;
    while(t--)
    {
        ans.clear();
        printf("Case #%d:\n", cas++);
        cin >> n >> l;
        string s = "1";
        dfs(s, 1);
        for(int i = 0; i < ans.size(); i++)
        {
            cout << ans[i];
            prin(ans[i]);
            puts("");
        }
    }
}
