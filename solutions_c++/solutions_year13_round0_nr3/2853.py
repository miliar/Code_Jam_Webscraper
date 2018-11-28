#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>
#include <cctype>
#include <string>

#define FOR(i, a, b) for(int i = a;i < b;++i)
using namespace std;

const int MAXN = 10005;
int T, M, N;

bool isP(int x)
{
    vector<int> a;
    while(x != 0)
    {
        a.push_back(x % 10);
        x /= 10;
    }
    for(int i = 0;i < a.size()/2;++i)
    {
        if(a[i] != a[a.size()-i-1]) return false;
    }
    return true;
}

int sqr[1005];
int P[1005];
void init()
{
    memset(sqr, -1, sizeof(sqr));
    for(int i = 1;i <= 1005;++i)
    {
        if(i * i > 1000)    continue;
        sqr[i*i] = i;
    }
    for(int i = 1;i <= 1005;++i)
    {
        if(isP(i))
        {
            P[i] = 1;
        }
    }
}

int isFS[1005];
int cnt[1005];
void solve()
{
    memset(isFS, 0, sizeof(isFS));
    for(int i = 1;i <= 1000;++i)
    {
        //printf("sqr[i] = %d\n",sqr[i]);
        if(sqr[i] > 0 && P[sqr[i]] && P[i])
        {
            isFS[i] = 1;
        }
        else isFS[i] = 0;
    }
    for(int i = 1;i <= 1000;++i)
    {
        if(isFS[i]) cnt[i] = cnt[i-1] + 1;
        else cnt[i] = cnt[i-1];
    }
}
int query(int a, int b)
{
    return cnt[b] - cnt[a-1];
}



int main()
{
    int a, b;
    init();
    solve();
    scanf("%d", &T);
    for(int t = 1;t <= T;++t)
    {
        printf("Case #%d: ", t);
        scanf("%d%d", &a, &b);
        printf("%d\n", query(a, b));
    }

}

