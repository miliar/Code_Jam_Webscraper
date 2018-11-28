#include "cstdio"
#include "cstring"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        int mat[5][5];
        bool there[17];
        
        int ra;
        memset(there, false, sizeof(there));
        
        scanf("%d",&ra);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&mat[i][j]);
        
        for(int i=0;i<4;i++)
            there[mat[ra-1][i]] = true;
        
        int ans,x;
        ans = 0;
        x = -1;
        
        scanf("%d",&ra);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&mat[i][j]);
        
        for(int i=0;i<4;i++)
        {
            if(there[mat[ra-1][i]])
            {
                ans++;
                x = mat[ra-1][i];
            }
        }
        
        printf("Case #%d: ",test);
        if(ans == 0)
            printf("Volunteer cheated!\n");
        else if(ans == 1)
            printf("%d\n",x);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
