/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
//int dx[]= {-1,0,1,0};
//int dy[]= {0,1,0,-1};
int r,c;
char G[105][105];
std::vector<pii> V;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("first-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 0;
    while(t--)
    {
        int ans = 0;
        cin >> r >> c;
        FOR(i,r)
        {
            scanf("%s",G[i]);
        }
        V.clear();
        FOR(i,r)
        FOR(j,c)
        {
            if(G[i][j] != '.')
            {
                int reqd = 10000000;
                if(G[i][j] == '^')
                {
                    for(int k=i-1;k>=0;k--)
                    {
                        if(G[k][j] != '.')
                        {
                            reqd = min(reqd,0);
                        }
                    }
                }
                else if(G[i][j] == 'v')
                {
                    for(int k=i+1;k<r;k++)
                    {
                        if(G[k][j] != '.')
                        {
                            reqd = min(reqd,0);
                        }
                    }
                }
                else if(G[i][j] == '>')
                {
                    for(int k=j+1;k<c;k++)
                    {
                        if(G[i][k] != '.')
                        {
                            reqd = min(reqd,0);
                        }
                    }
                }
                else if(G[i][j] == '<')
                {
                    for(int k=j-1;k>=0;k--)
                    {
                        if(G[i][k] != '.')
                        {
                            reqd = min(reqd,0);
                        }
                    }
                }
                for(int k=i-1;k>=0;k--)
                    {
                        if(G[k][j] != '.')
                        {
                            reqd = min(reqd,1);
                        }
                    }
                for(int k=i+1;k<r;k++)
                    {
                        if(G[k][j] != '.')
                        {
                            reqd = min(reqd,1);
                        }
                    }
                for(int k=j+1;k<c;k++)
                    {
                        if(G[i][k] != '.')
                        {
                            reqd = min(reqd,1);
                        }
                    }
                for(int k=j-1;k>=0;k--)
                    {
                        if(G[i][k] != '.')
                        {
                            reqd = min(reqd,1);
                        }
                    }
                ans += reqd;
                if(reqd > 1)
                {
                    break;
                }
            }
        }
        
        kas++;
        printf("Case #%d: ",kas);
        if(ans > 100000)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
return 0;
}
