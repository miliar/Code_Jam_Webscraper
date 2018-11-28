#include "cstdio"
#include "cstring"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    
    for(int test=1;test<=t;test++)
    {
        int board[102][102];
        int n,m;
        bool able=true;
        
        scanf("%d%d",&n,&m);
        
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)scanf("%d",&board[i][j]);
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                //printf("%d %d\n",i,j);
                
                bool abl;
                abl=true;
                
                for(int k=0;k<n;k++)
                {
                    if(board[i][j]<board[k][j])
                    {
                        //printf("lalala %d %d\n",board[i][j],board[k][j]);
                        abl=false;
                        break;
                    }
                }
                
                //printf("wew1\n");
                if(abl)continue;
                //printf("wew2\n");
                
                for(int k=0;k<m;k++)
                {
                        
                    if(board[i][j]<board[i][k])
                    {
                        able=false;
                        break;
                    }
                }
                
                if(!able)break;
            }
            if(!able)break;
        }
        
        printf("Case #%d: %s\n",test,(able)?"YES":"NO");
    }
    
    return 0;
}
