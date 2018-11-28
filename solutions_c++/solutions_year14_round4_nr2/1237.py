#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

int mx;
vector<int> v;
int dp[(1<<10)][11];
const int inf = (1<<30);

int calc(int mask, int last)
{
    if(mask == ((1<<v.size())-1)) return 0;
    int &ret = dp[mask][last];
    if(ret != -1) return ret;

    ret = inf;

    bool flag = false;
    int k = -1, cnt = 0;
    for(int i = 0;i<v.size();++i) if(mask & (1<<i))
    {
        if(v[i]==mx) flag = true;
        if(i==last) k = i;
    }

    if(!flag)
    {
        for(int i = 0;i<v.size();++i) if(!(mask&(1<<i)))
        {
            bool can = true;
            if(k!=-1 && v[k] > v[i]) can = false;
            if(can) ret = min(ret, calc(mask|(1<<i),i)+cnt);
            ++cnt;
        }
    }
    else
    {
        int best = -1, add = 0, id;
        for(int i = 0;i<v.size();++i) if(!(mask&(1<<i)))
        {
            if( v[i] > best )
            {
                best = v[i];
                add = cnt;
                id = i;
            }
            ++cnt;
        }
        ret = min(ret, calc(mask|(1<<id),id)+add);
    }
    return ret;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);

    int caseCnt = INPT_INT;

    for(int cNo = 1;cNo<=caseCnt;++cNo)
    {
        int N = INPT_INT;

        mx = 0;
        v.clear();
        for(int i = 0;i<N;++i) v.push_back(INPT_INT);

        for(int i = 0;i<N;++i) mx = max(mx,v[i]);

        memset(dp,-1,sizeof(dp));

        printf("Case #%d: ",cNo);
        printf("%d\n",calc(0,0));
    }
    return 0;
}
