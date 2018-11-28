#include<stdio.h>
#include<iostream>
#define gc() getchar()
int c;
#define read_int(n) n=0; c=gc();while(c<'0' || c>'9')c=gc();while(c>='0' && c<='9'){n= (n<<3)+(n<<1)+c-48;c=gc();}

using namespace std;

int main()
{
 int t,i=1;
 int a[5][5],b[5][5],ch1,ch2,j,k;


 read_int(t);
 while(i<=t)
 {
     int num,count=0,flag=0;

     read_int(ch1);

     for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)
         {
             read_int(a[j][k]);
         }
     }

    read_int(ch2);

    for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)
         {
             read_int(b[j][k]);
         }
     }
/*
printf("\nA:");

for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)
         {
             printf("%d  ",a[j][k]);
         }
         printf("\n");
     }

printf("\nB:");


     for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)
         {
             printf("%d  ",b[j][k]);
         }
         printf("\n");
     }

*/
     for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)
         {
            if(a[ch1-1][j]==b[ch2-1][k])
            {
                count++;
                num=a[ch1-1][j];
                if(count>=2)
                {
                 printf("Case #%d: Bad magician!\n",i);
                 flag=1;
                 break;
                }

            }
            if(flag==1)
            {
                break;
         }
         }
     }

     if(count==0)
        printf("Case #%d: Volunteer cheated!\n",i);

     else if(count==1)
     {
         printf("Case #%d: %d\n",i,num);
     }
     i++;
 }



return 0;
}
