#include<stdio.h>
#include<string.h>

int main()
{
 int T,S,cas=1,flag=0,flag1=0;  
 char K[1001];
 scanf("%i",&T);
 while(T--)
 {
           flag=0,flag1=0;
           scanf("%i %s\n",&S,K);
           //printf("%i %i\n",S,K[0]-48);
           flag1=K[0]-48;
           if(S==0)flag=0;
           else
           {
           for(int i=1;i<=S;i++)
           {
                   K[i]=K[i]-48;
                   if(flag1>=i)flag1=flag1+K[i];
                   else if(flag1<i)
                   {
                        flag=flag+(i-flag1);
                        flag1=K[i]+i;
                   }
                   //printf("%i   7 7 7\n",flag);
                   //printf("%i   8 8 8\n",flag1);
           }
           }
           printf("Case #%i: %i\n",cas++,flag);
 }  
    
}
