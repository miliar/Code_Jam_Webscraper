#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <math.h>
#include <limits>
#include <algorithm>

using namespace std;

bool isOk(int number, int si, int sj, vector<vector<int> > &grid)
{
    int n=grid.size();
    int m=grid[0].size();
    int i;
    int j;
    for (i=0; i<n; i++) if (grid[i][sj]>number) break;
    if (i==n) return 1;

    for (j=0; j<m; j++) if (grid[si][j]>number) break;
    if (j==m) return 1;

    return 0;
}


int main()
{
    freopen("blarge.in","r",stdin);
    freopen("blarge.out","w",stdout);
    int T,cas,n,m;
    cin>>T;
    for (cas=1; cas<=T; cas++)
    {
        cin>>n>>m;
        vector<vector<int> > grid(n,vector<int>(m));
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                cin>>grid[i][j];
            }
        }
        bool error=false;
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                if (!isOk(grid[i][j],i,j,grid)) error=true;
                if (error) break;
            }
            if (error) break;
        }
        if (error) printf("Case #%d: NO\n",cas);
        else printf("Case #%d: YES\n",cas);
    }
    return 0;
}
