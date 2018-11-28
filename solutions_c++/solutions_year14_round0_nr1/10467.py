#include<stdio.h>

int main(void)
{
    int cases, row[2], grid[2][4][4], ans,i,j,k,l,found,once,twice,num;
    scanf("%d",&cases);
    
    for(int i=0;i<cases;i++)
    {
        for(j=0; j<2; j++)
        {        
            scanf("%d", &row[j]); 
            for(k=0;k<4;k++)
            {
                for(l=0;l<4;l++)
                {
                     scanf("%d ", &grid[j][k][l]);    
                }
            }
        }
        
        once=0;twice=0;
        
        for(k=0;k<4;k++)
        {
            found=0;               
            num = grid[0][row[0]-1][k];
            for(l=0;l<4;l++)
            {
                if(num==grid[1][row[1]-1][l])
                {
                    found=1;                
                    ans=num;
                    break;
                }
            }
            if(found==1)
            {
                 if(once==1)
                 {
                     twice=1;
                     break;
                 }
                 else
                     once=1;
            }       
        }
        
        if(twice==1)
            printf("Case #%d: Bad magician!\n",i+1);            
        else if(once==1)
            printf("Case #%d: %d\n",i+1, ans);            
        else
            printf("Case #%d: Volunteer cheated!\n",i+1);            
    }
    
    return 0;   
}
