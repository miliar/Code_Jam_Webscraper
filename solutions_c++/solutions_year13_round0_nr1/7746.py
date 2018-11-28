#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
int test(char ch[4][5], char c)
{
    int i,j,k,p;
    for(i=0;i<4;i++)
    {
                    k=0;
                    p=0;
       for(j=0;j<4;j++)
       {
           if((ch[i][j]==c) || (ch[i][j]=='T'))
           k++;           
       }   
       if(k==4)
       return 1;
        for(j=0;j<4;j++)
       {
           if((ch[j][i]==c) || (ch[j][i]=='T'))
           p++;           
       }  
       if(p==4)
       return 1;           
    }
    k=0;p=0;
     for(j=0;j<4;j++)
       {
           if((ch[j][j]==c) || (ch[j][j]=='T'))
           k++; 
           if((ch[j][3-j]==c) || (ch[j][3-j]=='T'))
           p++;        
       }
       if((p==4)||(k==4))
       return 1;
       else
       return 0;
    
}
int draw(char ch[4][5])
{
    int i,j;
   for(i=0;i<4;i++)
   {
   for(j=0;j<4;j++)
   {
   if(ch[i][j]=='.')
     return 0;
   }  
  }  
  return 1;
}
main(){
       freopen("A-large.in","r",stdin);
       freopen("out.txt","w",stdout);
     int n,i,j,k,o,x;
     char  ch1[4][5];
     scanf("%d",&n);
     for(i=1;i<=n;i++)
     {
              scanf("%s",ch1[0]); 
              scanf("%s",ch1[1]);
              scanf("%s",ch1[2]);
              scanf("%s",ch1[3]); 
             if(test(ch1,'O'))
             printf("Case #%d: O won",i);
             else
             {
               if(test(ch1,'X'))
               printf("Case #%d: X won",i); 
               else
               {
                   if(draw(ch1))
               printf("Case #%d: Draw",i);
               else
                printf("Case #%d: Game has not completed",i);
               }
             }
             if(i<n)
             printf("\n");
     }
    
}
