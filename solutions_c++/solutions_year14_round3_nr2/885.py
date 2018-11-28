#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
using namespace std;
#define ll long long
ll gcd(ll a,ll b)
{
    int r;
    while(b>0)
    {
         r=a%b;
         a=b;
         b=r;
    }
    return a;
}
string str[105];
int n;
bool check(string ss)
{
    int site[128];
    for (int i = 'a'; i <= 'z'; ++i)
        site[i] = -1;
    int size = ss.size();
    int i ;
    for (i = 0; i < size; ++i)
    {
        if (site[ss[i]] == -1)
        {
            site[ss[i]] = i;
        }
        else if (site[ss[i]] != i - 1)
        {
            break;
        }
        else
        {
            site[ss[i]] = i;
        }

    }
    if (i < size)
        return false;
    else
        return true;
}
int  dfs(int deep, int zt, string ss)
{
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        if (zt&(1 << i))
            continue;
        string temp = ss + str[i];
        if (!check(temp))
            continue;
        if (deep == n - 1)
            ans += 1;
        else
            ans += dfs(deep+1, zt|(1<< i), temp);
    }
    return ans;
}
int main()
{
    freopen("B-small-attempt3.in","r", stdin);
    freopen("out.txt", "w", stdout);
    int cases;
    int cc =0;
    cin >> cases;
    while(cases--)
    {
        std::cerr << cc << endl;
        printf("Case #%d: ", ++cc);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            cin >> str[i];
        }
        int ans = dfs(0,0,"");
        cout << ans << endl;
    }
    return 0;
}
/*
有个类 Tools
tool.next_line()去获得下一行。
然后假如一行有int,double,int,struct test,
是不是调用 tool.get(a),tool.get(b),tool.get(c),tool.get(d)就行
*/
