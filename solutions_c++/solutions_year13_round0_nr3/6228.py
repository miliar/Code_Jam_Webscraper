#include<iostream>
#include<stdio.h>
#include<cmath>

int ispalindrome(int num)
{
    int n = num,rev=0,dig=0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if(n-rev==0)
        return  1;
    else
        return  0;
}

int main()
{
    int a,b,tc,ans,sqb,sqa;
    double sqra;
    scanf("%d",&tc);
    for(int t=1; t<=tc; t++)
    {
        ans=0;
        scanf("%d",&a);
        scanf("%d",&b);
        sqra = sqrt(a);
        sqb = sqrt(b);
        sqa = sqra;
        if(sqra-sqa)
            sqa+=1;
        
        for(int i=sqa; i<=sqb; i++)
        {
            if(ispalindrome(i)==1 && ispalindrome(i*i)==1)
                ans+=1;
        }
            
        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
