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


const int maxn = 10005;

int da[maxn];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ca++)
    {
        int n, x;
        scanf("%d%d", &n, &x);
        for(int i = 0; i < n; i++)
            scanf("%d", &da[i]);
        sort(da, da + n);
        int cnt = 0;
        int l = 0, r = n - 1;
        while(l <= r)
        {
            if(da[l] + da[r] <= x)
            {
                l++; r--;
            } else
            {
                if(da[l] > da[r]) l++;
                else r--;
            }
            cnt++;
        }
//        multiset<int> se;
//        for(int i = 0; i < n; i++)
//            se.insert(da[i]);
//        int cnt =  0;
//        for(int i = n - 1; i >= 0; i--)
//        {
//            if(se.find(da[i]) == se.end()) continue;
//            se.erase(da[i]);
//            cnt++;
//            set<int>::iterator it = se.upper_bound(x - da[i]);
//            if(it != se.begin())
//            {
//                it--;
//                se.erase(it);
//            }
//        }
        printf("Case #%d: %d\n", ca, cnt);
    }
    return 0;
}
