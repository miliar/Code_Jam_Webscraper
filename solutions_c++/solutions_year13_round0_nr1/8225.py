#include<stdio.h>
void printd(int ans)
{
    if(ans==1)
    printf("X won\n");
    else if(ans==2)
    printf("O won\n");
    
    return;
}



int main()
{
    int t,i1;
    scanf("%d",&t);
    getchar();
    for(i1=1;i1<=t;i1++)
    {
        printf("Case #%d: ",i1);
        int a[4][4]={0},b[4][4]={0},i,j,ans=-1,pending=0;
        char text;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%c",&text);
                
                if(text=='X')
                {
                a[i][j]=1;
                b[i][j]=1;
                }
                
                else if(text=='O')
                {
                a[i][j]=2;
                b[i][j]=2;
                }
                
                else if(text=='.')
                {
                a[i][j]=0;
                b[i][j]=0;
		pending=1;

                }
                
                else if(text=='T')
                {
                a[i][j]=1;
                b[i][j]=2;
                }
else 
j--;
            }
        }
       /* for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
printf("%d ",b[i][j]);
}
printf("\n");
}*/
                
                for(i=0;i<4;i++)
                {
                    if(a[i][0]==0)
                    continue;
                    if(a[i][0]==a[i][1] && a[i][1]==a[i][2] && a[i][2]==a[i][3] )
                    ans=a[i][0];
                    else if(b[i][0]==b[i][1] && b[i][1]==b[i][2] && b[i][2]==b[i][3] )
                    ans=b[i][0];
                }
                
                
                if(ans!=-1)
                {
                    printd(ans);
                    continue;
                    
                }
                for(j=0;j<4;j++)
                {
                    if(a[0][j]==0)
                    continue;
                    if(a[0][j]==a[1][j] && a[1][j]==a[2][j] && a[2][j]==a[3][j] )
                    ans=a[0][j];
                    else if(b[0][j]==b[1][j] && b[1][j]==b[2][j] && b[2][j]==b[3][j] )
                    ans=b[0][j];
                }
                
                
                if(a[0][0]!=0 && a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[2][2]==a[3][3] )
                ans=a[0][0];
                else if(b[0][0]!=0 && b[0][0]==b[1][1] && b[1][1]==b[2][2] && b[2][2]==b[3][3] )
                ans=a[0][0];
                else if(a[3][0]!=0 && a[3][0]==a[2][1] && a[2][1]==a[1][2] && a[1][2]==a[0][3] )
                ans=a[3][0];
                else if(b[3][0]!=0 && b[3][0]==b[2][1] && b[2][1]==b[1][2] && b[1][2]==b[0][3] )
                ans=b[3][0];
                if(ans!=-1)
                {
                    printd(ans);
                    continue;
                }
                
                else if(ans==-1)
                {
                    if(pending==1)
                    printf("Game has not completed\n");
                    else
                    printf("Draw\n");
                    
                }
                
                
                
                    
                    
                    
                    
                    
            }
            return 0;
        }
                
                
                
                
                
                
                
                
                
        
        
        
        
        
        
        
        
    
    
    
    
    