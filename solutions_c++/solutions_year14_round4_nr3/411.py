#include <iostream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;


const int MAX = 1010;
int to[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
int mapp[1010][1010];
int n, m;
int clk;
int dfs(int u, int v, int d) {
    if (mapp[u][v] != 0) return false;
    if (v+1==m) {
        mapp[u][v] = clk;
        return 1;
    }
    for (int k = d+1+4; k>= d-1+4; k--) {
        int tx = u + to[k%4][0], ty = v + to[k%4][1];
        if (tx < 0 || tx >= n || ty < 0 || ty >= m) continue;
        mapp[u][v] = -2;
        if (dfs(tx, ty, k%4)) {
            mapp[u][v] = clk;
            return 1;
        }
    }
    return false;
}

struct node
{
    int value;
    int position;
};

node p[MAX];
int po[MAX];

struct cmp
{
    bool operator()(const node &na, const node &nb)
    {
        return na.value > nb.value;
    }
};


int main() {
    int i,j,k,t,Case = 1;
    cin>>t;
    while(t--)
    {
        priority_queue<node, vector<node>, cmp> q;
        int k;
        cin>>n>>m>>k;
        memset(mapp, 0, sizeof(mapp));
        for(int tt=0; tt < k; tt++){
            int x1, y1, x2, y2;
            cin>>x1>>y1>>x2>>y2;
            for (i = x1; i <= x2; i++)
                for (j = y1; j <= y2; j++)
                    mapp[i][j] = -1;
        }
        int ans = 0;
        clk = 0;
        for (i = 0; i < n; i++)
        {
            clk++;
            if (dfs(i, 0, 0)) ans++;
        }
        cout<<"Case #"<<Case++<<": "<<ans<<endl;
    }
    return 0;
}
