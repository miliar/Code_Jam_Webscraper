//mdm

#include<stdio.h>

int main()
{
  int test;
  scanf("%d",&test);
  char arr[4][4];
  arr[0][0]='h';
  arr[0][1]='i';
  arr[0][2]='j';
  arr[0][3]='k';
  arr[1][0]='i';
  arr[1][1]='H';
  arr[1][2]='k';
  arr[1][3]='J';
  arr[2][0]='j';
  arr[2][1]='K';
  arr[2][2]='H';
  arr[2][3]='i';
  arr[3][0]='k';
  arr[3][1]='j';
  arr[3][2]='I';
  arr[3][3]='H';
  

  char str[10055];
  long long x;
  long long y;
  int i;
 /* for(i=0;i<4;i++)
    for(int  j=0;j<4;j++)
       printf("%c\n",arr[i][j]);*/
  for(i=1;i<test+1;i++)
  {
     scanf("%lld %lld",&x,&y);
     scanf("%s",str);
     int progress=0;
     char last[1];
     last[0]=' ';
     long long j,k;
     int neg=0;
     for(j=0;j<y;j++)
     { 
       for(k=0;k<x;k++)
       {
         if(last[0]==' '){
           last[0]=str[k];
           if(last[0]=='i')
             progress=1;
         }
         else
         {
           last[0]=arr[last[0]-'h'][str[k]-'h'];
           if(last[0]=='H')
           {
             last[0]='h';
             neg=(neg+1)%2;
           }else if(last[0]=='I')
           {
             last[0]='i';
             neg=(neg+1)%2;
           }else if(last[0]=='J')
           {
             last[0]='j';
             neg=(neg+1)%2;
           }
           else if(last[0]=='K')
           {
             last[0]='k';
             neg=(neg+1)%2;
           }
           
           //printf("%c\n",last[0]);
           if(last[0]=='i')
           {
             if(progress==0)
               progress=1;
           }
           if(last[0]=='k')
           {
             if(progress==1)
               progress=2;
           }
       }}
     }
     if((last[0]=='h')&&(neg==1))
     {
       if(progress==2)
         printf("Case #%d: YES\n",i);
       else
         printf("Case #%d: NO\n",i);
     }
     else
       printf("Case #%d: NO\n",i);
}
return 0;
}
