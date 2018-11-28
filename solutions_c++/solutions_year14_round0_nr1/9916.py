#include<stdio.h>
int main()
{
    int t=0,i,j,k,a1,a2,sol,z=0;
    int arr1[4][4],arr2[4][4];
    scanf("%d",&t);
    while (z<t)
    {
         int m=0;
         scanf("%d",&a1);
         for(int r=0;r<4;r++)
         {
                 for(int c=0;c<4;c++)
                 {
                        scanf("%d",&arr1[r][c]);
                       // printf("%d",arr1[r][c]);
                 }
         }
         scanf("%d",&a2);
         for(int r=0;r<4;r++)
         {
                 for(int c=0;c<4;c++)
                 {
                        scanf("%d",&arr2[r][c]);
                         //                       printf("%d",arr2[r][c]);
                 }
         }
         for(int r=0;r<4;r++)
         {
                         for(int c=0;c<4;c++)
                         {
                                         if(arr1[a1-1][r]==arr2[a2-1][c])
                                         {//printf("\n%d %d",arr1[a1-1][r],arr2[a2-1][c]);
                                         sol=arr1[a1-1][r];
                                         m+=1;
                                         //printf("\n %d",m);
                                         }
                         }                                   
         }
         if(m==1)
         printf("Case #%d: %d\n",z+1,sol);
         else if(m>1)
         printf("Case #%d: Bad magician!\n",z+1);
         else 
         printf("Case #%d: Volunteer cheated!\n",z+1);
         z++;
         }
         return 0;
         }
