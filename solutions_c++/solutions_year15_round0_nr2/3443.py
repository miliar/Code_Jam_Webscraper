#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>
#include<set>
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;
#define MP(i,j) make_pair(i,j)
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> PII;

int T,tt,n,r,s,ans,a[1005];

template <class T>void up(T&a,T b){if(a<b)a=b;}
template <class T>void down(T&a,T b){if(a>b)a=b;}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    for (scanf("%d", &T); T; T--)
    {
        printf("Case #%d: ", ++tt);
        scanf("%d", &n);
        r = 1;
        for (int i = 1; i <= n; i++)
          scanf("%d", &a[i]), up(r, a[i]);
        ans = r;
        for (int i = 1; i <= r; i++)
        {
            s = 0;
            for (int j = 1; j <= n; j++)
              s += (a[j] - 1) / i;
            down(ans, s + i);
		}
		printf("%d\n", ans);
    }
    return 0;
}
