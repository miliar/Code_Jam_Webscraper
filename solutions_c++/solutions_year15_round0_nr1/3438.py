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

int a[maxn];
char str[maxn];
int n;

int main()
{
    int i,j,t,cas=1;
    freopen("C:/Users/asus1/Downloads/A-large.IN","r",stdin);
    freopen("F:/≥Ã–Ú…Ëº∆/ACM/CF&&BC/Google/out.txt","w",stdout);
    sf(t);
    while (t--)
    {
        sf(n);
        scanf("%s",str);
        FRE(i,0,n)
            a[i]=str[i]-'0';
         int ans=0;
         int num=a[0];
         FRE(i,1,n)
         {
             if (num<i)
             {
                 ans=ans+(i-num);
                 num=num+(i-num);
             }
             num+=a[i];
         }
         pf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}

/*
2
1 10

*/
