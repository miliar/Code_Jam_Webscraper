#pragma comment(linker, "/STACK:1677721600")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <algorithm>
#define pb push_back
#define mp make_pair
#define LL long long
#define lson lo,mi,rt<<1
#define rson mi+1,hi,rt<<1|1
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define mem(a,b) memset(a,b,sizeof(a))
#define FIN freopen("B-large.in", "r", stdin)
#define FOUT freopen("B-large.out", "w", stdout)
#define rep(i,a,b) for(int i=(a); i<=(b); i++)
#define dec(i,a,b) for(int i=(a); i>=(b); i--)

using namespace std;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const double ee = exp(1.0);
const int inf = 0x3f3f3f3f;
const int maxn = 1e6 + 10;
const double pi = acos(-1.0);

int readT()
{
    char c;
    int ret = 0,flg = 0;
    while(c = getchar(), (c < '0' || c > '9') && c != '-');
    if(c == '-') flg = 1; else ret = c ^ 48;
    while( c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c ^ 48);
    return flg ? - ret : ret;
}

LL readTL()
{
    char c;
    int flg = 0;
    LL ret = 0;
    while(c = getchar(), (c < '0' || c > '9') && c != '-');
    if(c == '-') flg = 1; else ret = c ^ 48;
    while( c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c ^ 48);
    return flg ? - ret : ret;
}

int main()
{
    #ifdef LOCAL
    FIN;
    FOUT;
    #endif // LOCAL
    int ncase = readT();
    int ca = 1;
    while (ncase--)
    {
        string str;
        cin >> str;
        stack<char> s;
        s.push('+');
        for (int i = str.length() - 1; i >= 0; --i)
        {
            if (str[i] == s.top())
            {
                continue;
            }
            else
            {
                s.push(str[i]);
            }
        }
        int po = 0;
        int ne = 0;
        char now = s.top();
        s.pop();
        while (!s.empty())
        {
            if (s.top() == '+')
            {
                if (now == '-')
                {
                    ne++;
                    now = '+';
                }
            }
            else
            {
                po++;
            }
            s.pop();
        }
        int ans = po * 2 + ne;
        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
