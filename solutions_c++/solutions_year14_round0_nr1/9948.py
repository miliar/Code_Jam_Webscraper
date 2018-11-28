#include<stdio.h>
#include<string.h>

int main()
{   int testcase,a1,a2,i,j,c1[50][50],c2[50][50],hasil,z,x=1,flag,k,l;
    scanf("%i",&testcase);
    while(testcase--)
    {                flag=0;
                     hasil=0;
                     scanf("%i",&a1);
                     for(i=0;i<4;i++)
                     {               for(j=0;j<4;j++)
                                     {
                                                     scanf("%i",&c1[i][j]);           
                                     }               
                     }
                     scanf("%i",&a2);
                     for(i=0;i<4;i++)
                     {               for(j=0;j<4;j++)
                                     {
                                                     scanf("%i",&c2[i][j]);           
                                     }               
                     }
                     for(k=0;k<4;k++)
                     {               for(l=0;l<4;l++)
                                     {               if(c1[a1-1][k]==c2[a2-1][l])
                                                     {                              hasil=c1[a1-1][k];
                                                                                    flag++;
                                                     }
                                     }               
                     }
                     if(flag>1)
                     {         printf("Case #%i: Bad magician!\n",x++);                           }
                     else if(flag==0)
                     {         printf("Case #%i: Volunteer cheated!\n",x++);                      }
                     else
                     printf("Case #%i: %i\n",x++,hasil);
    }
}
