#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
bool vis[12];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ncase, tcase = 1, n, i, j, k;
    scanf("%d", &ncase);
    while(ncase--)
    {
        scanf("%d", &n);
        if(n == 0) printf("Case #%d: INSOMNIA\n", tcase++);
        else
        {
            mem(vis);
            for(i = 1; i <= 100; i++)
            {
                int tmp = n*i;
                while(tmp)
                {
                    vis[tmp%10] = 1;
                    tmp /= 10;
                }
                for(j = 0; j < 10; j++)
                {
                    if(vis[j] == 0) break;
                }
                if(j == 10) break;
            }
            printf("Case #%d: %d\n", tcase++, n*i);
        }
    }
    return 0;
}
