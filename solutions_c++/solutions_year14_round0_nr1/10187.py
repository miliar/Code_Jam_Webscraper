

#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int t,n1, n2,i,j,k,l,m, x=0, y=0, a[4][4], b[4][4];
    scanf("%d",&t);
    for(i=0; i<t; i++)
    {
             scanf("%d", &n1);
             for(j=0;j<4;j++)
             {
                             for(k=0;k<4;k++)
                             {
                                             scanf("%d",&a[j][k]);
                             }
             }
             scanf("%d", &n2);
             for(j=0;j<4;j++)
             {
                             for(k=0;k<4;k++)
                             {
                                             scanf("%d",&b[j][k]);
                             }
             }  
             
             for(l=0;l<4;l++)
             {
                             for(m=0;m<4;m++)
                             {
                                             if(a[n1-1][l]==b[n2-1][m])
                                             {
                                                                   if(x==0)
                                                                           x=a[n1-1][l];
                                                                   else
                                                                           y=a[n1-1][l];
                                             }
                             }
             }
             if((x==0)&&(y==0))
                     printf("Case #%d: Volunteer cheated!\n", i+1);
             else if(x!=0&&y==0)
                     printf("Case #%d: %d\n",i+1,x);
             else if(y!=0)
                     printf("Case #%d: Bad magician!\n",i+1);
             x=0;
             y=0;
    }
    return 0;
}
             
             
                                                                                                                                           
