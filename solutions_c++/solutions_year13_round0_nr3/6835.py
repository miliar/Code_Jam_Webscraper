#include<stdio.h>
#include<math.h>
#include<iostream.h>

using namespace std;

int palindrome(int i)
{
    int m,rev=0,temp;
    temp=i;
    while(i)
    {
            m=i%10;
            rev=(rev*10)+m;
            i=i/10;
    }
    if(temp==rev)
    {
               return 1;
    }
    return 0;
}

int main()
{
    freopen("C-small-attempt0.IN", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, beg,end,i,count=0;
    scanf("%d", &n);
    int j;
    double x;
    for(j=0; j<n; j++)
    {
             printf("Case #%d: ", j+1);
             count = 0;
             scanf("%d%d",&beg,&end);
             for(i=beg;i<=end;i++)
             {
                                  if(palindrome(i))
                                  {
                                                   x = sqrt(i);
                                                   if((x-(int)x)==0)
                                                   if(palindrome(x))
                                                   {
                                                                    count++;
                                                   }
                                  }
             }
             printf("%d\n", count);
    }
    return 0;
}
