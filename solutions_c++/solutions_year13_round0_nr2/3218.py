#include<stdio.h>

int n,m;
int data[110][110];

void input()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            scanf("%d",&data[i][j]);
        }    
    }    
}    

int HON(int x,int target)
{
    for(int j=0;j<m;j++)
    {
        if(data[x][j]>target)
          return 0;
    }    
    return 1;
}    

int VER(int y,int target)
{
    for(int i=0;i<n;i++)
    {
        if(data[i][y]>target)
            return 0;
    }    
    return 1;
}    

int analysis()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(!(HON(i,data[i][j])||VER(j,data[i][j])))
            {
                return 0;
            }    
        }    
    }    
    return 1;
}    

int main()
{
   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d %d",&n,&m);
        input();
        printf("Case #%d: ",i+1);
        if(analysis())
        {
            printf("YES\n");
        }else{
            printf("NO\n");
        }        
    }    
    return 0;
}    
