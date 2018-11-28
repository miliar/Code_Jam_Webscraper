#include<stdio.h>
#include<math.h>

int isPalindrome(int n)
{   //Palindrome return 1; Not Palindrome return 0;
    char buf[1005];
    sprintf(buf,"%d",n);
    int l=0;
    while(buf[l]!='\0') l++;
    for(int i=0;i<(l/2);i++)
    {
        if(buf[0+i]!=buf[l-1-i]) return 0;
    }
    return 1;
}

void check(int k,int a,int b)
{
    int count=0;
    for(int i=a;i<=b;i++)
    {
        if(isPalindrome(i))
        {
            if(sqrt(i)==floor(sqrt(i)))
            {
                if(isPalindrome(floor(sqrt(i))))
                {
                    //printf("%d ",i);
                    count++;
                }
            }
        }
    }
    //printf("\n");
    printf("Case #%d: %d\n",k,count);
}

int main()
{
    int i,j,k,n,t,a,b,fre;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&a);
        //scanf("%ld",&fre);
        scanf("%d",&b);
        //printf("%d %d\n",a,b);
        check(k,a,b);
    }

    return 0;
}
