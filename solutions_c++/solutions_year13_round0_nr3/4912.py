#include<stdio.h>
#include<conio.h>
#include<math.h>

int check_palindrome(int n)
{
 int s=0,p;
 p=n;
 while(p>0)
 {
           s=10*s+(p%10);
           p=p/10;
           
           }  
    if(s==n)
    return 1;
    return 0;
}

int sqr(int n)
{
    int i;
 for(i=1;i*i<=n;i++);
 i--;
 printf("\n%d",i);
 if(i*i==n)
 return i;
 return 122;
    
}


int main()
{
 int i,j,k,a,b,z;
 FILE *f1,*f2;
 f1=fopen("input.txt","r");   
  f2=fopen("out.txt","w");   
    
    fscanf(f1,"%d",&k);
    printf("%d",k);
    for(i=1;i<=k;i++)
    {
                     
                     fscanf(f1,"%d",&a);
                     fscanf(f1,"%d",&b);
                     
                     j=0;
                     for(z=a;z<=b;z++)
                     if(check_palindrome(z) && check_palindrome(sqr(z)))
                     j++;
                     fprintf(f2,"Case #%d: %d\n",i,j);
                     }
    
    getch();
}
