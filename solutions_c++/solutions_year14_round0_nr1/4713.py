#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,r1,r2;
    int k = 1;
    int g[5][5];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&r1);
        for(int i=1;i<5;i++)
            for(int j=1;j<5;j++)
                scanf("%d",&g[i][j]);
        vector<int>buf;
        for(int i=1;i<5;i++)
            buf.push_back(g[r1][i]);
        scanf("%d",&r2);
        vector<int>buf2;
        for(int i=1;i<5;i++)
            for(int j=1;j<5;j++)
                scanf("%d",&g[i][j]);
        int cnt = 0;
        int ans;
        for(int i=0;i<buf.size();i++)
            for(int j=1;j<5;j++)
            {
                if(buf[i] == g[r2][j])
                {
                    cnt++;
                    ans = buf[i];
                }
            }
        if(cnt == 1)
            printf("Case #%d: %d\n",k++,ans);
        else if ( cnt > 0)
            printf("Case #%d: Bad magician!\n",k++);
        else
            printf("Case #%d: Volunteer cheated!\n",k++);
    }
    return 0;
}
