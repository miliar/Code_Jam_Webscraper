
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <functional>
#include <stack>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;

typedef long long ll;
const double eps = 1e-6;
const int maxint = -1u>>2;

int n,m;

int dui[5][10];
int pdui[5];

int ans,ans_cnt;
const int MOD = 1000000007;
string str[10];

void calc()
{
    for(int i=1;i<=n;i++)
    {
        if(pdui[i] == 0)
        {
            return ;
        }
    }
    int tmp = 0;
    for(int i=1;i<=n;i++)
    {
        set<string> st;
        st.clear();
        st.insert("");
        for(int j=0;j<pdui[i];j++)
        {
            for(int k=0;k<str[dui[i][j]].length();k++)
            {
                st.insert(str[dui[i][j]].substr(0, k+1));
            }
        }
        tmp += st.size();
        if(tmp > ans)
        {
            ans = tmp;
            ans_cnt = 1;
        }
        else if(tmp == ans)
        {
            ans_cnt = (ans_cnt + 1)%MOD;
        }
    }

}

void doit(int pos)
{
    if(pos > m)
    {
        calc();
        return ;
    }
    for(int i=1;i<=n;i++)
    {
        dui[i][pdui[i]++] = pos;
        doit(pos+1);
        pdui[i]--;
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        memset(dui, 0, sizeof(dui));
        memset(pdui, 0, sizeof(pdui));
        ans = 0;
        ans_cnt = 0;

        scanf("%d%d",&m,&n);
        for(int i=1;i<=m;i++)
        {
            cin>>str[i];
        }
        doit(1);
        printf("Case #%d: %d %d\n", cas, ans, ans_cnt);
    }

    return 0;
}


