//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<cmath>
#include<climits>
#include<string>
#include<map>
#include<queue>
#include<vector>
#include<stack>
#include<set>
#include<ctime>
//#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define pb(a) push(a)
#define INF 0x1f1f1f1f
#define lson idx<<1,l,mid
#define rson idx<<1|1,mid+1,r
#define PI  3.1415926535898
template<class T> T min(const T& a, const T& b, const T& c)
{
    return min(min(a, b), c);
}
template<class T> T max(const T& a, const T& b, const T& c)
{
    return max(max(a, b), c);
}
void debug()
{
#ifdef ONLINE_JUDGE
#else
    freopen("in.txt","r",stdin);
    // freopen("d:\\out1.txt","w",stdout);
#endif
}
int getch()
{
    int ch;
    while((ch = getchar()) != EOF)
    {
        if(ch!=' ' && ch!='\n') return ch;
    }
    return EOF;
}


const int maxn = 1005;
int a[maxn];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ca++)
    {
        int n;
        scanf("%d", &n);
        int maxv = -INF;
        for(int i = 1; i <= n; i++)
        {
            scanf("%d", &a[i]);
            maxv = max(maxv, a[i]);
        }

        int x[maxn];
        for(int i = 1; i <= n; i++)
            x[i] = i;
        int ans = INF;
        sort(x + 1, x + 1 + n);
        do
        {
            int flag = 1;
            for(int i = 1; i <= n; i++)
            {
                if(a[x[i]] == maxv)
                {
                    for(int j = i; j > 1; j--)
                    {
                        if(a[x[j]] < a[x[j - 1]])
                            flag = 0;
                    }
                    for(int j = i; j < n; j++)
                    {
                        if(a[x[j]] < a[x[j + 1]])
                            flag = 0;
                    }
                    if(flag)
                    {
                        int cnt = 0;
                        for(int i = 1; i <= n; i++)
                        {
                            for(int j = i + 1; j <= n; j++)
                            {
                                if(x[j] < x[i]) cnt++;
                            }
                        }
                        ans = min(ans, cnt);
                    }
                    break;
                }
            }
        }while(next_permutation(x + 1, x + 1 + n));
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
