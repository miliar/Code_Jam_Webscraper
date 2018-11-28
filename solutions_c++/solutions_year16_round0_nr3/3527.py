#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define push push_back
int n,gcj;

void dfs(string &s,int x)
{
    if(gcj == 0)
        return ;
    if(x == n)
    {
        vector<long long > vec;
        s = s + "1";
        for(int i = 2; i <= 10; ++i)
        {
            long long tmp = 0;
            for(int j = 0; j < n; j++)
            {
                tmp = tmp * i + s[j] - '0';
            }
            for(int j = 2; j <= tmp / j; ++j)
            {
                if(tmp % j == 0)
                {
                    vec.push(j);
                    break;
                }
            }

        }
        if(vec.size() == 9)
        {
            gcj--;
            cout << s;
            for(int i = 0; i < vec.size(); ++i)
            {
                printf(" ");
                cout << vec[i];
            }
            puts("");
        }
        return;
    }
    string tmp = s + "0";
    dfs(tmp,x + 1);
    tmp = s + "1";
    dfs(tmp,x + 1);
}

void solve()
{
    int T,kcase = 1;
    cin>>T;
    while(T--)
    {
        cin>>n>>gcj;
        printf("Case #%d:\n",kcase++);
        string s = "1";
        dfs(s,2);
    }
}

int main() {
    //freopen("in","r",stdin);
    //freopen("A.out","w",stdout);
    solve();
    return 0;
}
