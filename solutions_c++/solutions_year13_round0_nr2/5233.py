#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>

#define SQR(x) ((x)*(x))
#define LL long long int
#define LLU long long unsigned
#define pb push_back
#define pp pop_back
#define MP make_pair
#define sz size()
#define VI vector<int>
#define QI queue<int>
#define SI stack<int>
#define ff first
#define ss second
#define MII map<int, int>
#define SD(a) scanf("%d", &a)
#define SD2(a, b) scanf("%d %d", &a, &b)
#define NL puts("")
#define CLR(a) memset(a, 0, sizeof(a))
#define SET(a) memset(a, -1, sizeof(a))
#define rep(i, init, n) for(i=init; i<n; i++)
#define repv(i, init, n) for(i=init; i>n; i--)
#define rep1(i, init, n) for(i=init; i<=n; i++)
#define repv1(i, init, n) for(i=init; i>=n; i--)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define MAXN 10010
#define EPS 1e-9
#define INF 2147483647
#define MOD 747474747
#define pi acos(-1.0)
using namespace std;
int arr[105][105], row[105], col[105];
int main()
{
    //READ("B-large.in");
    //WRITE("output.txt");
    int ncase, tcase, n, m, i, j, flag;
    SD(ncase);
    rep1(tcase, 1, ncase)
    {
        SD2(n, m);
        CLR(row);
        CLR(col);
        rep(i, 0, n)
        {
            rep(j, 0, m)
            {
                SD(arr[i][j]);
                row[i]=max(row[i], arr[i][j]);
                col[j]=max(col[j], arr[i][j]);
            }
        }
        flag=1;
        rep(i, 0, n)
        {
            rep(j, 0, m)
            {
                if(arr[i][j]!=row[i] && arr[i][j]!=col[j])
                {
                    flag=0;
                    break;
                }
            }
        }
        printf("Case #%d: ", tcase);
        if(flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
