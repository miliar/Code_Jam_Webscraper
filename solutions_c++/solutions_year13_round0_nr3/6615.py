#include<stdio.h>

bool ispalindrome(int num)
{
    int digits=0,start,end;
    int a[10];
    
    while(num!=0)
    {
        a[digits++]=(num%10);
        num=(num/10);
    }
    start=0;
    end=digits-1;
    
    while(start<end)
    {
        if(a[start]!=a[end])
        return 0;
        start++;
        end--;
    }
    return 1;
}
    

int main()
{
    int i,a[1050]={0},count=0;
    for(i=1;i<=32;i++)
    {
        if(ispalindrome(i) && (ispalindrome(i*i)))
        {
            a[i*i]=1;
            //printf("%d\n",i*i);
        }
        
    }
    for(i=1;i<=1000;i++)
    {
        if(a[i]==1)
        count++;
        a[i]=count;
        
    }
    a[0]=0;
    int t,i1,a1,b1;
    scanf("%d",&t);
    for(i1=1;i1<=t;i1++)
    {
        printf("Case #%d: ",i1);
        scanf("%d%d",&a1,&b1);
        printf("%d\n",a[b1]-a[a1-1]);
    }
    
    
    return 0;
}
    
    
    

