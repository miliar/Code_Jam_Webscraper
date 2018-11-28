#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <stack>
#include <vector>
#include <set>
#include <queue>
#pragma comment (linker,"/STACK:102400000,102400000")
#define maxn 10005
#define MAXN 2005
#define mod 1000000009
#define INF 0x3f3f3f3f
#define pi acos(-1.0)
#define eps 1e-6
#define lson rt<<1,l,mid
#define rson rt<<1|1,mid+1,r
#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FREE(i,a,b) for(i = a; i >= b; i--)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define FRLL(i,a,b) for(i = a; i > b; i--)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pf          printf
#define DBG         pf("Hi\n")
typedef long long ll;
using namespace std;

int p[maxn];
int d;

int main()
{
    int i,j,t,cas=1;
//    freopen("C:/Users/asus1/Downloads/B-large.IN","r",stdin);
//    freopen("F:/≥Ã–Ú…Ëº∆/ACM/CF&&BC/Google/out.txt","w",stdout);
    sf(t);
    while (t--)
    {
        sf(d);
        int maxx=0;
        int ans=INF;
        FRL(i,0,d)
        {
            sf(p[i]);
            maxx=max(maxx,p[i]);
        }
        FRE(i,1,maxx)
        {
            int num=0;
            FRL(j,0,d)
            {
                int x=p[j]/i+(p[j]%i==0?0:1)-1;
                num+=x;
            }
            ans=min(ans,num+i);
        }
        pf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
