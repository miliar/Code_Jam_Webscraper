#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#define pb push_back
#define mp make_pair
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;
const int maxn = 110;
char ditu[maxn][maxn];
int r,c;
bool search(int x,int y)
{
    int cnt = 0;
    for(int i=0; i<c; i++) if(ditu[x][i] != '.') cnt++;
    if(cnt > 1) return true;
    cnt = 0;
    for(int i=0; i<r; i++) if(ditu[i][y] != '.') cnt++;
    if(cnt > 1) return true;
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%d%d",&r,&c);
        for(int i=0; i<r; i++)
            scanf("%s",ditu[i]);
        printf("Case #%d: ",cas);
        int ans = 0;
        for(int i=0; i<r && ans >=0; i++)
        {
            for(int j=0; j<c && ans >= 0; j++)
            {
                if(ditu[i][j]!='.')
                {
                    if(ditu[i][j] == '<')
                    {
                        bool flag = false;
                        for(int k=j-1; k>=0 && !flag; k--)
                        {
                            if(ditu[i][k] != '.') flag = true;
                        }
                        if(!flag)
                        {
                            flag = search(i,j);
                            if(flag) ans++;
                            else ans = -1;
                        }
                    }
                    else if(ditu[i][j] == '>')
                    {
                        bool flag = false;
                        for(int k=j+1; k<c && !flag; k++)
                        {
                            if(ditu[i][k] != '.') flag = true;
                        }
                        if(!flag)
                        {
                            flag = search(i,j);
                            if(flag) ans++;
                            else ans = -1;
                        }
                    }
                    else if(ditu[i][j] == '^')
                    {
                        bool flag = false;
                        for(int k=i-1; k>=0 && !flag; k--)
                        {
                            if(ditu[k][j] != '.') flag = true;
                        }
                        if(!flag)
                        {
                            flag = search(i,j);
                            if(flag) ans++;
                            else ans = -1;
                        }
                    }
                    else
                    {
                        bool flag = false;
                        for(int k=i+1; k<r && !flag; k++)
                        {
                            if(ditu[k][j] != '.') flag = true;
                        }
                        if(!flag)
                        {
                            flag = search(i,j);
                            if(flag) ans++;
                            else ans = -1;
                        }
                    }
                }
            }
        }
        if(ans < 0) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
