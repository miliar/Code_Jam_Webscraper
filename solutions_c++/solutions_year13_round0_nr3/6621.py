#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<math.h>
int cal(int a, int b);
int square(int x);
int pallindrom(int x);
int digit(int x);
int input()
{
    int x,i,index,j;
    int a[100][2];
    FILE *fp;

     FILE *fp1;
     if((fp1=freopen("C-small-attempt0.in","r",stdin))==NULL)
     {
         printf("Cannot open file.\n");
         exit(1);
     }
     scanf("%d",&index);
     for(i=0;i<index;i++){
     j=0;
		      while(scanf("%d",&a[i][j++])==1 && j<2)
		      {
		      }
              }
     
     fclose(fp1);
    if((fp=freopen("OUT2", "w" ,stdout))==NULL) {
    printf("Cannot open file.\n");
    exit(1);
    }
     i=0;
		      while(i<index)
		      {
                    //    printf("%d %d\n",a[i][0],a[i][1]);
                          x=cal(a[i][0],a[i][1]);
                          printf("Case #%d: %d\n",i+1,x);
                        i=i+1;
              } 
    fclose(fp);
    
    return 0;
}
int digit(int x)
{
    int i,digit=0;
    while(x>0)
    {
       
        digit=digit+1;
        x=x/10;
       
    }
    return digit;
}
int pallindrom(int x)
{
    int mul=1,z=0,y=x,i;
    int d = (digit(x)-1);
    while(d>0)
    {
               mul=mul*10;
               d=d-1;
    }
 
    while(x!=0)
    {
        i=x%10;
        z=z+i*mul;
        mul=mul/10;
        x=x/10;
 
    }
    if(y==z)
    {
            return 0;
    }
    else
    {
        return 1;
    }
}
int square(int x)
{
    int i,z;
    i=(int)sqrt(x);
    //printf("\nsq = %d\n",i);
    while(i>0)
    {
        z=i*i;
        if(z==x)
        {
 
                return i;
        }
        else
        {
            i=i-1;
        }
    }
    return 0;
}
int cal(int a, int b)
{
 
    int i=a,x,y,z,count=0;
    while(i<=b)
    {
               x=pallindrom(i);
               if(x==0)
               {
                       y=square(i);
                       if(y!=0)
                       {
                              z=pallindrom(y);
                              if(z==0)
                              {
                                       count =count +1;
                              }
                       }
               }
               i=i+1;
    }
    return count;
}
int main()
{
    input();
    getch();
    return 0;
}
