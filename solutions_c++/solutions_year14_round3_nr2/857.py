#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int n;
string s[1001];
int a[1001];
int b[1001];
int c;

inline char last(string &s)
{
    return s[s.length() - 1];
}

inline char first(string &s)
{
    return s[0];
}

inline void test()
{
    string ss = "";
    for(int i = 1 ; i <= n ; i++)
        ss += s[a[i]];
    int t[26] = {0};
    for(int i = 0 ; i < 26 ; i++)
        t[i] = -1;
    for(int i = 0 ; i < ss.length() ; i++)
    {

        if(t[ss[i] - 'a'] == i - 1 || t[ss[i] - 'a'] == -1)
        {
            t[ss[i] - 'a'] = i;

        }
        else
        {
            return;
        }
    }
    c++;
}

void dfs(int k)
{
    if(k > n)
    {
        test();
        return;
    }
    for(int i = 1 ; i <= n ; i++)
    if(b[i] == 0)
    {
        b[i] = 1;
        a[k] = i;
        //if(k == 1 || last(s[a[k - 1]]) == first(s[i]))
        {
            dfs(k + 1);
        }
        b[i] = 0;
    }
}

void work()
{
    c = 0;
    for(int i = 1 ; i <= n ; i++)
    {
        b[i] = 0;
    }
    dfs(1);
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int ttt;
    cin >> ttt;
    for(int tt = 1 ; tt <= ttt ; tt++)
    {
        cin >> n;
        for(int i = 1 ; i <= n ; i++)
            cin >> s[i];
        cout << "Case #" << tt << ": ";
        work();
        cout << c << endl;
    }
    return 0;
}
