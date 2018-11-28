#include<stdio.h>
#include<conio.h>
#include<math.h>

int palindrome(int x)
{
    int digit,temp,rev=0;
    temp=x;
    
    while(temp>0)
    {
      digit=temp%10;
      rev=(rev*10)+digit;
      temp=temp/10;
    }
    if(rev==x)return 1;
  return 0;
}

int main()
{
    int i,a[31],no,A,B,m,n,l,j,k,count;
    
    for(i=1;i<=31;i++)
      a[i]=i*i;
    scanf("%d",&no);
    for(i=0;i<no;i++)
    {
                    count=0;
                    scanf("%d %d",&A,&B);
                    m=sqrt(A);
                    if((m*m)==A)
                       j=m;
                    else 
                       j=m+1;
                    n=sqrt(B);
                      k=n;
                    for(l=j;l<=k;l++)
                    {
                                     if(palindrome(a[l]))
                                     {
                                         if(palindrome(l))
                                            count++;
                                     }
                    
                    }                   
                     printf("Case #%d: %d\n",i+1,count);
    }
    getch();
    return 0;
}
