#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
#include <queue>
#include <algorithm>
#include <cmath>
//#include <unordered_map>
//#define lson x<<1
//#define rson x<<1|1
//#define mid ((lt[x].l+lt[x].r)/2)
//#define ID(x, y) ((x)*m+(y))
#define CHECK(x, y) ((x)>=0 && (x)<n && (y)>=0 && (y)<m)
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
#define pb push_back
#define Vector Point
#define LD long long double
const int INF=0x3f3f3f3f;
void Open()
{
        freopen("A-small-attempt2.in","r",stdin);
        freopen("A-small-attempt2.out","w",stdout);
    #ifndef ONLINE_JUDGE
        //freopen("/home/qingping/in.txt","r",stdin);
//        freopen("D:/my.txt","w",stdout);
    #endif // ONLINE_JUDGE
}
const int N = 10020;
int n;
int sta[111];
int tmp[111];
int beat[] = {1, 2, 0};
int r, p, s;
bool check()
{
    memcpy(tmp, sta, sizeof(sta));
    int resn = n;
    while(resn > 1)
    {
        for(int i = 0; i < resn; i += 2)
        {
            if(tmp[i] == tmp[i+1]) return false;
            if(beat[tmp[i]] == tmp[i+1])
                tmp[i/2] = tmp[i];
            else
                tmp[i/2] = tmp[i+1];
        }
        resn /= 2;
    }
    return resn == 1;
}
bool dfs(int dep, int cr, int cp, int cs)
{
    if(cr > r || cp > p || cs > s) return false;
    if(dep == n)
    {
        return check();
    }
    for(int i = 0; i < 3; i++)
    {
        sta[dep] = i;
        int sr = cr, sp = cp, ss = cs;
        if(i == 0) sp++;
        if(i == 1) sr++;
        if(i == 2) ss++;
        if(dfs(dep+1, sr, sp, ss)) return true;
    }
    return false;
}
int main()
{
//    Open();
    int T;
    scanf("%d", &T);
    int cas = 1;
    while(T--)
    {
        scanf("%d", &n);
        n = 1 << n;
        scanf("%d%d%d", &r, &p, &s);
        printf("Case #%d: ", cas++);
        if(dfs(0, 0, 0, 0)) {
            for(int i = 0 ; i < n; i++)
            {
                printf("%c", "PRS"[sta[i]]);
            }
            printf("\n");
        }else{
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
