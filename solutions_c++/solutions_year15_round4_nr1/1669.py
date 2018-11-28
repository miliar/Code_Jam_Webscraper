#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)
#define F first
#define S second
#define mp make_pair
#define LL long long
#define pb push_back
using namespace std;
#define sz 300005
#define inf 0x7fffffff
int dx[] = {0,0,-1,1};
int dy[] = {-1,1,0,0};
int r,c;
string a[105];
int v[105][105];
int num,sum;
int row[105],col[105];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).out","w",stdout);
    int t;
    cin>>t;
    rep(cas,t){

        cin>>r>>c;
        rep(i,r)
            cin>>a[i];

        memset(v,0,sizeof(v));

        num = 0;

        memset(row,0,sizeof(row));
        memset(col,0,sizeof(col));
        rep(i,r)
            rep(j,c)
                if(a[i][j]!='.')
                    row[i]++;
        rep(i,c)
            rep(j,r)
                if(a[j][i]!='.')
                    col[i]++;
        int flag = 0;
        rep(i,r)
            rep(j,c)
                if(a[i][j]!='.' && row[i]==1 && col[j]==1)
                    flag = 1;

        sum = 0;
        rep(x,r)rep(y,c)
        {
            if(a[x][y]=='.')continue;
            int dir = 1;
            if(a[x][y] == '^')
                dir = 2;
            if(a[x][y] == 'v')
                dir = 3;
            if(a[x][y] == '<')
                dir = 0;
            int cx = x;
            int cy = y;
             cx = cx + dx[dir];
             cy = cy + dy[dir];

            while(cx>=0 && cy>=0 && cx<r && cy<c && a[cx][cy]=='.')
            {
                cx = cx + dx[dir];
                cy = cy + dy[dir];
            }
            if(cx>=0 && cy>=0 && cx<r && cy<c);
            else sum++;
        }
        if(flag == 1)
        {
            cout << "Case #" << cas+1 << ": IMPOSSIBLE" <<endl;
        }
        else
        {
            cout << "Case #" << cas+1 << ": " << sum  <<endl;
        }
    }
}
/*
10
3 3
<..
.><
..<
2 2
.<
.<
2 2
<>
<.
3 3
<>.
...
.<>
*/
