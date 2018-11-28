#include <stdio.h>

int main()
{
    int data[4][4];
    int result[4];
    int cases;
    scanf("%d",&cases);
    int counter=1;
    int i,j,k;
    int row;
    int cek=0;
    int angka;
    while(cases-->0)
    {
        for(k=0;k<2;k++)
        {
            scanf("%d",&row);
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    scanf("%d ",&data[i][j]);    
                }
            }
            if(k==1)
            {
                for(j=0;j<4;j++)
                {
                    for(i=0;i<4;i++)
                    {
                        if(result[j]==data[row-1][i])
                        {
                            cek=cek+1;
                            angka=result[j]; 
                        }         
                    }
                }
                if(cek==1)
                {
                    printf("Case #%d: %d\n",counter,angka);    
                }
                else if(cek>1)
                {
                    printf("Case #%d: Bad magician!\n",counter);    
                }
                else if(cek==0)
                {
                    printf("Case #%d: Volunteer cheated!\n",counter);    
                }
                cek=0;   
            }
            else
            {
                for(j=0;j<4;j++)
                {
                    result[j]=data[row-1][j];    
                }    
            }
        }
       
        counter++;
    }
    
    return 0;    
}
