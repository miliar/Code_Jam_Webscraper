/**
used Codeblocks C++ lang ( free online )
**/
#include <cstdio>
#include <cstring>

using namespace std;
int ap[20],mat[20][20],row,tstcase;

void solve()
{
    memset(ap,0,sizeof(ap));
    for(int k = 1; k <= 2; ++k)
    {
        scanf("%d",&row);
        for(int i = 1; i <= 4; ++i)
        {
            for(int j = 1; j <= 4; ++j)
            {
                scanf("%d",&mat[i][j]);
                if(row == i) /// the gwessed one first
                    ap[mat[i][j]] ++;
            }
        }
    }
    int cnt = 0,possible = 0;
    for(int i = 1; i <= 16; ++i)
        if(ap[i] == 2){
            ++cnt;
            possible = i;
        }
    if(cnt == 1) /// bini di tat
        printf("Case #%d: %d\n",tstcase,possible);
    else
        if(cnt > 1)
            printf("Case #%d: Bad magician!\n",tstcase);
        else
            printf("Case #%d: Volunteer cheated!\n",tstcase);
}

int main()
{
    freopen("magictrick.in","r",stdin);
    freopen("magictrick.txt","w",stdout);

    int T;
    scanf("%d",&T);
    while(T--)
    {
        ++tstcase;
        solve();
    }
    return 0;
}
