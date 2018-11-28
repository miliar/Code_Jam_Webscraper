#include<stdio.h>
int main()
{
    int a[5][5],b[5][5],k,i,j,t,row1,row2,count,index,num=1;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
                    count=0;
                    scanf("%d",&row1);
                    for(j=0;j<4;j++)
                    {
                                    for(k=0;k<4;k++)
                                    {
                                                    scanf("%d",&a[j][k]);
                                    }
                    }
                    scanf("%d",&row2);
                    for(j=0;j<4;j++)
                    {
                                    for(k=0;k<4;k++)
                                    {
                                                    scanf("%d",&b[j][k]);
                                    }
                    }
                    for(j=0;j<4;j++)
                    {
                                    for(k=0;k<4;k++)
                                    {
                                                    if(a[row1-1][j]==b[row2-1][k])
                                                    {
                                                                                count++;
                                                                                index=j;
                                                    }
                                    }
                    }
                    if(count==0)
                    {
                                printf("Case #%d: Volunteer cheated!\n",num++);
                    }
                    else
                    {
                        if(count>1)
                        {
                           printf("Case #%d: Bad magician!\n",num++); 
                        }
                        else
                        {
                            if(count==1)
                            {
                                        printf("Case #%d: %d\n",num++,a[row1-1][index]);
                            }
                        }
                    }
    }
    return 0;
}
                    
                    
