#include <stdio.h>
#include <string.h>
int tcase,loop,ans=2147483647,len;
int hash[3000];
char str[110];
void f(int cnt)
{
    int i,j,h,digit;
    char temp;
    
    if(ans<=cnt)
        return;
    
    for(i=0;i<len;i++)
    {
        if(str[i]=='-')
            break;
    }
    if(i==len)
    {
        if(ans>cnt)
            ans=cnt;
        return;
    }
    
    for(i=0;i<len;i++)
    {
        for(j=0;j<=i/2;j++)
        {
            temp=str[j];
            str[j]=str[i-j];
            str[i-j]=temp;
        }
        for(j=0;j<=i;j++)
        {
            if(str[j]=='+')
                str[j]='-';
            else
                str[j]='+';
        }
        
        h=0; digit=1;
        for(j=0;j<len;j++)
        {
            if(str[j]=='+')
                h+=digit;
            digit*=2;
        }
        if(hash[h]>cnt+1)
        {
            hash[h]=cnt+1;
            f(cnt+1);
        }
        
        for(j=0;j<=i/2;j++)
        {
            temp=str[j];
            str[j]=str[i-j];
            str[i-j]=temp;
        }
        for(j=0;j<=i;j++)
        {
            if(str[j]=='+')
                str[j]='-';
            else
                str[j]='+';
        }
        
    }
}
int main()
{
    int i;
    freopen("B-small-attempt0.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d",&tcase);
    
    for(loop=1;loop<=tcase;loop++) {
        
        scanf("%s",str);
        len = strlen(str);
        
        for(i=0;i<3000;i++)
            hash[i]=2147483647;
        ans=2147483647;
        
        f(0);
        
        printf("Case #%d: %d\n",loop,ans);
        
    }
    return 0;
}