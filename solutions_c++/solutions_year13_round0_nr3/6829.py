#include<stdio.h>
#include<conio.h>
#include<math.h>
int palindrome(int x)
{
    int temp,z=0;
    temp=x;
    while(x!=0)
    {
        z=z*10+x%10;
        x=x/10;
    }
    if(temp==z)
    return 1;
    else 
    return 0;
}

int fns(int a)
{
    float sq=sqrt(a);
    
    if(sq-(int)sq==0)
    {
        if(palindrome(a)==1)
        {
            if(palindrome(sq)==1)
            return 1;
        }
        else 
            return 0;
    }     
    return 0;
}

int main()
{
    int t,i,a,b, count, x;
    
    FILE *ptr = fopen("input.txt", "r");
    FILE *ptr2 = fopen("output.txt", "w");
    
    
    //printf("Enter test cases   ");
    fscanf(ptr, "%d",&t);
    for(x=1;x<=t;x++)
    {
        fscanf(ptr, "%d %d",&a,&b);
        count=0;
        for(i=a;i<=b;i++)
        {
            if(fns(i)==1)
                count++;
        }
        fprintf(ptr2,"Case #%d: %d\n", x, count);
    }
    getch();
    return 0;
}
    
