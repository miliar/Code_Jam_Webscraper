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
int T,tt,n,s;
char st[1005];
bool bj;
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
        scanf("%d%s", &n, st);
        for (int i = 0; i <= n; i++)
        {
            s = i;
            bj = 1;
            for (int j = 0; j <= n; j++)
            {
                if (s < j)
                {
                    bj = 0;
                    break;
                }
                s += st[j] - '0';
            }
            if (bj)
            {
                printf("%d\n", i);
                break;
            }
        }
    }
    return 0;
}
