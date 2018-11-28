#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
// Let's Fight!

const int MAXN = 111;
const int dx[] = { 1,-1, 0, 0};
const int dy[] = { 0, 0, 1,-1};
const char dc[] = {'v', '^', '>', '<'};

int R, C;

char arr[MAXN][MAXN];

int calc()
{
    int ans = 0;
    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
        {
            if(arr[i][j] == '.')
                continue;

            bool notedge = false;
            bool canself = false;
            for(int k=0; k<4; k++)
            {
                int ii = i, jj = j;
                bool other = false;
                while(1)
                {
                    int ni = ii + dx[k], nj = jj + dy[k];
                    if(ni < 0 || ni >= R || nj < 0 || nj >= C) break;
                    if(arr[ni][nj] != '.') other = true;
                    ii = ni;
                    jj = nj;
                }
                if(other)
                {
                    notedge = true;
                    if(arr[i][j] == dc[k])
                        canself = true;
                    continue;
                }
            }
            if(!notedge) return -1;
            if(!canself) ans++;
        }
    }
    return ans;
}

int main()
{
    IOS;
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++)
    {
        cin>>R>>C;

        for(int i=0; i<R; i++)
            cin>>arr[i];

        int ans = calc();
        
        cout<<"Case #"<<tt<<": ";
        if(ans==-1) cout<<"IMPOSSIBLE";
        else cout<<ans;
        cout<<endl;
    }
    return 0;
}
