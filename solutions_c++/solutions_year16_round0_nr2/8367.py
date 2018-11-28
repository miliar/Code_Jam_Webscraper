#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const int N = 110;
char str[N];

char s[] = "-+";

int dfs(int len, int flag)
{
    int ans = 0;
    if(len == 0)
    {
        return str[len] != s[flag];
    }
    if(str[len] == s[flag])
    {
        return dfs(len-1, flag);
    }
    else
    {
        return dfs(len-1, !flag)+1;
    }
}

int main(void)
{
    int T;
    freopen("B-large.in", "r", stdin);
    freopen("ou.txt", "w", stdout);
    cin >> T;
    int cnt = 1;
    while(T--)
    {
        cin >> str;
        int len = strlen(str);
//        printf("Case #%d: %d\n",cnt++,dfs(len-1, 1));
        cout << "Case #" << cnt++ <<": " << dfs(len-1, 1) << endl;
//        cout << dfs(len-1, 1) << endl;
    }
    return 0;
}
