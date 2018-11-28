#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int ch[30];
string num[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int n[10], cur;
bool dfs()
{
    if(cur == 0) return true;
    for(int i = 0; i < 10; i++)
    {
        bool f = true;
        for(int j = 0; j < num[i].length(); j++)
        {
            ch[num[i][j] - 'A']--;
            if(ch[num[i][j] - 'A'] == 0)
                cur--;
        }
        for(int j = 0; j < num[i].length(); j++)
        {
            if(ch[num[i][j] - 'A'] < 0)
            {
                f = false;
                break;
            }
        }
        if(f)
        {
            n[i]++;
            if(dfs()) return true;
            n[i]--;
        }
        for(int j = 0; j < num[i].length(); j++)
        {
            if(ch[num[i][j] - 'A'] == 0)
                cur++;
            ch[num[i][j] - 'A']++;
        }
    }
    return false;
}
int main()
{
    freopen("A-small-attempt2.in","r", stdin);
    freopen("a.out","w", stdout);
    int t;
    cin >> t;
    for(int ti = 1; ti <= t; ti++)
    {
        string str;
        cin >> str;
        memset(ch, 0, sizeof(ch));
        memset(n, 0, sizeof(n));
        cur = 0;
        for(int i = 0; i < str.length(); i++)
        {
            if(ch[str[i] - 'A'] == 0)
                cur++;
           ch[str[i] - 'A']++;
        }
        dfs();
        printf("Case #%d: ", ti);
        for(int i = 0; i < 10; i++)
        {
            while(n[i] > 0)
            {
                cout << i;
                n[i]--;
            }
        }
        cout << endl;
    }
    return 0;
}
